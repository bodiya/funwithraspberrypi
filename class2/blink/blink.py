#Fun with Raspberry Pi by Brian Bodiya & Tom Amlicke is licensed under a
#Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
#Based on a work at https://github.com/bodiya/funwithraspberrypi.
#
#Copyright Brian Bodiya & Tom Amlicke, 2014
#
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT)

led_on = False
try:
  while 1:
    led_on ^= True
    GPIO.output(22, led_on) 
    time.sleep(1)
except KeyboardInterrupt:
  GPIO.cleanup()
