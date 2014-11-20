#Fun with Raspberry Pi by Brian Bodiya & Tom Amlicke is licensed under a
#Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
#Based on a work at https://github.com/bodiya/funwithraspberrypi.
#
#Copyright Brian Bodiya & Tom Amlicke, 2014
#
import RPi.GPIO as GPIO
import threading
from Tkinter import *
from rotary import *

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(25,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

#display variables
canvas_height = 500
canvas_width = 500
bg_color = "black"
x = canvas_width/2
y = canvas_height/2
color = "white"
line_width = 5
line_length = 5

#rotary encoder variables
last_wheel_status = 0
wheel_status_lock = threading.Lock()
move_lock = threading.Lock()
vertical = False
right_move = 0b10110100
left_move  = 0b01111000

#wheel functions

def channel_active(channel):
  wheel_status_lock.acquire()
  global last_wheel_status

  #when using GPIO.BOTH, you can't see which edge you're on,
  #so you must read the pin again
  current_status = GPIO.input(channel)
  last_status = get_last_status(last_wheel_status)
  #print "Channel %i active: status(%i),last_status(%i)" % (channel,current_status,last_status)
  
  new_status = get_new_status_threaded(current_status, last_status, channel)
  
  #even with bouncetime=1, we might encounter bounce, better safe than sorry
  if last_status == new_status:
    wheel_status_lock.release()
    return
  
  #update the last wheel status
  last_wheel_status = get_new_wheel_status(last_wheel_status, new_status)

  #release the lock on last_wheel_status, then execute the move
  wheel_status_lock.release()
  execute_move(last_wheel_status,vertical)

def button_pressed(channel):
  global vertical
  print "Button pressed!"
  vertical ^= True

def execute_move(last_status,vertical):
  right = (last_status == right_move)
  left  = (last_status == left_move)
  if vertical and right:
    move_N()
  elif vertical and left:
    move_S()
  elif right:
    move_E()
  elif left:
    move_W()

#controls 
def move_N(self=None):
  with move_lock:
    global y
    canvas.create_line(x, y, x, (y-line_length), width=line_width, fill=color)
    y = y - line_length
 
def move_S(self=None):
  with move_lock:
    global y
    canvas.create_line(x, y, x, y+line_length, width=line_width, fill=color)
    y = y + line_length
 
def move_E(self=None):
  with move_lock:
    global x
    canvas.create_line(x, y, x + line_length, y, width=line_width, fill=color)
    x = x + line_length
 
def move_W(self=None):
  with move_lock:
    global x
    canvas.create_line(x, y, x - line_length, y, width=line_width, fill=color)
    x = x - line_length

#interrupts
GPIO.add_event_detect(23, GPIO.RISING, callback=button_pressed, bouncetime=300)
GPIO.add_event_detect(24, GPIO.BOTH, callback=channel_active, bouncetime=1)
GPIO.add_event_detect(25, GPIO.BOTH, callback=channel_active, bouncetime=1)

#main program
window = Tk()
window.title("Pi-Etch-A-Sketch")
canvas = Canvas(bg=bg_color, height=canvas_height, width=canvas_width, highlightthickness=0)
canvas.pack()

##debug using arrow keys
#window.bind("<Up>", move_N)
#window.bind("<Down>", move_S)
#window.bind("<Left>", move_W)
#window.bind("<Right>", move_E)

try:
  window.mainloop()
  GPIO.cleanup()
except KeyboardInterrupt:
  GPIO.cleanup()

