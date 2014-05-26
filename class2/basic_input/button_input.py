#Fun with Raspberry Pi by Brian Bodiya & Tom Amlicke is licensed under a
#Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
#Based on a work at https://github.com/bodiya/funwithraspberrypi.
#
#Copyright Brian Bodiya & Tom Amlicke, 2014
#
import RPi.GPIO as GPIO
#import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

pressed = 0
try:
  while 1:
    status = GPIO.input(23) 
    if status == 1 and pressed == 0:
      print "Button pressed!"
      pressed = 1
    elif status == 0:
      pressed = 0
      #time.sleep(0.001)
except KeyboardInterrupt:
  GPIO.cleanup()
