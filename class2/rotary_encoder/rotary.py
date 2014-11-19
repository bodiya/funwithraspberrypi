#Fun with Raspberry Pi by Brian Bodiya & Tom Amlicke is licensed under a
#Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
#Based on a work at https://github.com/bodiya/funwithraspberrypi.
#
#Copyright Brian Bodiya & Tom Amlicke, 2014
#
import RPi.GPIO as GPIO

def read_wheel(last_wheel_status):
  left_status = GPIO.input(24) 
  right_status = GPIO.input(25)
  new_status = left_status | right_status << 1
  last_status = (last_wheel_status & 0b00000011)
  if new_status != last_status:
    #print "New status: %i" % (new_status)
    last_wheel_status = new_status | ((last_wheel_status << 2) & 0b0011111111)
  return last_wheel_status

def read_button(last_button_status,vertical):
  button_status = GPIO.input(23) 
  if button_status != last_button_status:
    last_button_status = button_status
    if button_status == 1:
      print "Button pressed!"
      vertical ^= True
  return (vertical,last_button_status)

