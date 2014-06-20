#Fun with Raspberry Pi by Brian Bodiya & Tom Amlicke is licensed under a
#Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
#Based on a work at https://github.com/bodiya/funwithraspberrypi.
#
#Copyright Brian Bodiya & Tom Amlicke, 2014
#
import smbus
import time

bus = smbus.SMBus(1)

address = 0x48 # address of PCF8591P
Vref = 4.3
convert = Vref / 256
channel = 0 # 0,1,2, or 3 valid

print "Read the A/D channel %i" % channel
print "print reading when it changes"
print "Ctrl C to stop"

# Set the control register to read from the specified channel
bus.write_byte(address, channel)

last_reading = -1
while True: 
  try:
    reading = bus.read_byte(address)
    #only trip on a decently large change
    #use read_analog.py to determine what's appropriate
    if(abs(last_reading - reading) > 10):
      #print "A/D reading %i meaning %.2fV" % (reading,(convert * reading))
      if (last_reading > reading):
        print "\nWho turned the lights OFF?!"
      else:
        print "\nWho turned the lights ON?!"
      last_reading = reading
    time.sleep(2)
  except KeyboardInterrupt:
    print "\nExiting."
    exit(0)
  except:
    e = sys.exc_info()[0]
    print "Error:\n%s" % e
    print "Aborting\n"
    exit(1)

