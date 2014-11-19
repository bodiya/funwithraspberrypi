#Fun with Raspberry Pi by Brian Bodiya & Tom Amlicke is licensed under a
#Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
#Based on a work at https://github.com/bodiya/funwithraspberrypi.
#
#Copyright Brian Bodiya & Tom Amlicke, 2014
#
import RPi.GPIO as GPIO
from Tkinter import *
from rotary import read_wheel, read_button

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
last_button_status = 0
vertical = False
right_move = 0b10110100
left_move  = 0b01111000

def read_encoder():
  global last_button_status
  global vertical
  vertical,last_button_status = read_button(last_button_status,vertical)
  
  global last_wheel_status
  new_wheel_status = read_wheel(last_wheel_status)
  if new_wheel_status != last_wheel_status:
    last_wheel_status = new_wheel_status
    #print "last_wheel_status = %d" % last_wheel_status
    execute_move(last_wheel_status,vertical)
  window.after(1,read_encoder)

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
  global y
  canvas.create_line(x, y, x, (y-line_length), width=line_width, fill=color)
  y = y - line_length
 
def move_S(self=None):
  global y
  canvas.create_line(x, y, x, y+line_length, width=line_width, fill=color)
  y = y + line_length
 
def move_E(self=None):
  global x
  canvas.create_line(x, y, x + line_length, y, width=line_width, fill=color)
  x = x + line_length
 
def move_W(self=None):
  global x
  canvas.create_line(x, y, x - line_length, y, width=line_width, fill=color)
  x = x - line_length

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

#give the window a second to finish being drawn before looking for input
window.after(1000,read_encoder)

try:
  window.mainloop()
  GPIO.cleanup()
except KeyboardInterrupt:
  GPIO.cleanup()

