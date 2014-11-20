#Fun with Raspberry Pi by Brian Bodiya & Tom Amlicke is licensed under a
#Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
#Based on a work at https://github.com/bodiya/funwithraspberrypi.
#
#Copyright Brian Bodiya & Tom Amlicke, 2014
#
import RPi.GPIO as GPIO

####################
#for first exercise
####################

def read_wheel(last_wheel_status):
  new_status = get_new_status()
  last_status = get_last_status(last_wheel_status)
  if new_status != last_status:
    #print "New status: %i" % (new_status)
    last_wheel_status = get_new_wheel_status(last_wheel_status, new_status)
  return last_wheel_status

def read_button(last_button_status,vertical):
  button_status = GPIO.input(23)
  if button_status != last_button_status:
    last_button_status = button_status
    if button_status == 1:
      print "Button pressed!"
      vertical ^= True
  return (vertical,last_button_status)

def get_last_status(last_wheel_status):
  return last_wheel_status & 0b00000011

def get_new_wheel_status(last_wheel_status, new_status):
  return new_status | ((last_wheel_status << 2) & 0b0011111111)

def get_new_status():
  return GPIO.input(24) | GPIO.input(25) << 1

####################
#for second exercise
####################

#bit masks to *or* when a pin becomes active, or *and* when a pin
#becomes inactive
pin_masks = {24: [0b01,0b10],
             25: [0b10,0b01]}

def get_new_status_threaded(current_status, last_status, channel):
  #determine the new position using the last reading of the other pin,
  #plus the current reading
  if current_status:
    return last_status | pin_masks[channel][0]
  else:
    return last_status & pin_masks[channel][1]
