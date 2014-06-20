# Output a count to the D/A in the PCF8591P @ address 74
from smbus import SMBus
from time import sleep

# comment out the one that does not apply to your board
bus = SMBus(1) # for revision 2 boards
address = 0x48
control = 1<<6 # enable analog output

print("Output a ramp on the D/A")
print("Ctrl C to stop")

try:
  modifier = 1
  a = 100
  while True:
    #TODO: make the LED even *more* pleasing by having the
    #intensity follow a sine wave, rather than just increase/decrease
    #at a linear rate.
    bus.write_byte_data(address, control, a) # output to D/A
    sleep(0.01)
    a += modifier
    if a < 100 or a > 254:
      modifier *= -1
except KeyboardInterrupt:
  bus.write_byte_data(address, control, 0)
  print "Resetting Analog Out to 0. Exiting."
  exit()
