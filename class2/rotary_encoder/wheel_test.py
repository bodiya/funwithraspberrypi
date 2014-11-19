#Fun with Raspberry Pi by Brian Bodiya & Tom Amlicke is licensed under a
#Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
#Based on a work at https://github.com/bodiya/funwithraspberrypi.
#
#Copyright Brian Bodiya & Tom Amlicke, 2014
#
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(25,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

last_status = 0
last_button_status = 0
try:
  while 1:
    left_status = GPIO.input(24) 
    right_status = GPIO.input(25) 
    new_status = left_status | right_status << 1
    if new_status != last_status:
      print "New status: %i" % (new_status)
      last_status = new_status
      
    button_status = GPIO.input(23) 
    if button_status != last_button_status:
      last_button_status = button_status
      if button_status == 1:
        print "Button Pressed!"
except KeyboardInterrupt:
  GPIO.cleanup()
