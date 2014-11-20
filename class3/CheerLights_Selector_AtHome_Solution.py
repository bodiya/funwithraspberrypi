#Fun with Raspberry Pi by Brian Bodiya & Tom Amlicke is licensed under a
#Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
#Based on a work at https://github.com/bodiya/funwithraspberrypi.
#
#Copyright Brian Bodiya & Tom Amlicke, 2014
#
import random
import RPi.GPIO as GPIO
import sys
import threading
import time
from twython import Twython

#Set the pinout
GPIO.setmode(GPIO.BCM)

#define the pins
RED_PIN = 22
GREEN_PIN = 27
BLUE_PIN = 17
L_WHEEL_PIN = 25
R_WHEEL_PIN = 24
BUTTON_PIN = 23

#Set the pin modes and create PWM objects for the LED
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

pwmRed = GPIO.PWM(RED_PIN, 500)
pwmRed.start(100)

pwmGreen = GPIO.PWM(GREEN_PIN, 500)
pwmGreen.start(100)

pwmBlue = GPIO.PWM(BLUE_PIN, 500)
pwmBlue.start(100)

#Set the pin modes for the Rotary Encoder
GPIO.setup(BUTTON_PIN,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(R_WHEEL_PIN,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(L_WHEEL_PIN,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

API_KEY = '***************YOUR DATA*****************'
API_SECRET = '***************YOUR DATA*****************'
ACCESS_TOKEN = '***************YOUR DATA*****************'
ACCESS_TOKEN_SECRET = '***************YOUR DATA*****************'

color_intensities = {'red': [100,0,0],
                     'green': [0,100,0],
                     'blue': [0,0,100],
                     'cyan': [0,100,100],
                     'white': [100,100,100],
                     'warmwhite': [99,96,90],
                     'purple': [50,0,50],
                     'magenta': [100,0,100],
                     'yellow': [100,100,0],
                     'orange': [100,65,0],
                     'pink': [100,75,80],
                     'oldlace': [99,96,90]}

colors = color_intensities.keys()

verbs = ['demands','requests','would like','desires','pines for']
adjectives = ['beautiful','awesome','pretty','gross','evil','aweful']

api = Twython(API_KEY,API_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET) 


#rotary encoder variables
last_wheel_status = 0
wheel_status_lock = threading.Lock()
color_lock = threading.Lock()
current_color = 0

def send_color():
  with color_lock:
    color = colors[current_color]
    verb = verbs[random.randrange(0,len(verbs))]
    adjective = adjectives[random.randrange(0,len(adjectives))]
    new_status = '@cheerlights My Pi %(verb)s the %(adjective)s color %(color)s' % \
                 {"color"     : color,
                  "verb"      : verb,
                  "adjective" : adjective}
    print "Updating status to:\n%s" % new_status
    api.update_status(status=new_status)
    print "Color successfully changed to %s" % color

def change_LED():
  global pwmRed
  latest_color = colors[current_color]
  print("Changing color to: " + latest_color)
  pwmRed.ChangeDutyCycle(color_intensities[latest_color][0])
  pwmGreen.ChangeDutyCycle(color_intensities[latest_color][1])
  pwmBlue.ChangeDutyCycle(color_intensities[latest_color][2])

#bit masks to *or* when a pin becomes active,
#or *and* when a pin becomes inactive
pin_masks = {R_WHEEL_PIN: [0b01,0b10],
             L_WHEEL_PIN: [0b10,0b01]}

def channel_active(channel):
  wheel_status_lock.acquire()
  global last_wheel_status

  #when using GPIO.BOTH, you can't see which edge you're on,
  #so you must read the pin again
  current_status = GPIO.input(channel)
  last_status = (last_wheel_status & 0b00000011)

  #determine the new position using the last reading of the other pin,
  #plus the current reading
  if current_status:
    new_status = last_status | pin_masks[channel][0]
  else:
    new_status = last_status & pin_masks[channel][1]
  
  #we're bound to encounter some bounce, make sure the new reading
  #is actually new
  if last_status == new_status:
    wheel_status_lock.release()
    return
  
  #update the last wheel status
  last_wheel_status = new_status | ((last_wheel_status << 2) & 0b0011111111)
  new_status = last_wheel_status

  #release the lock on last_wheel_status, then execute the move
  wheel_status_lock.release()
  
  right_move = 0b10110100
  left_move  = 0b01111000
  with color_lock:
    global current_color
    if(new_status == right_move):
      current_color += 1
    elif(new_status == left_move):
      current_color -= 1
    else:
      return
    current_color %= len(colors)
    change_LED()

#interrupts
GPIO.add_event_detect(R_WHEEL_PIN,
                      GPIO.BOTH,
                      callback=channel_active,
                      bouncetime=1)
GPIO.add_event_detect(L_WHEEL_PIN,
                      GPIO.BOTH,
                      callback=channel_active,
                      bouncetime=1)

while 1:
  try:
    #blocking interrupt for the button press
    GPIO.wait_for_edge(BUTTON_PIN, GPIO.FALLING)
    send_color()
    time.sleep(0.3)
  except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit(0)
  except:
    e = sys.exc_info()[0]
    print "Error:\n%s" % e
    print "Continuing in one second...\n"
    time.sleep(1)
