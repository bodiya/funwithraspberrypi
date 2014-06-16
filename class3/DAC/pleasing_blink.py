# Output a count to the D/A in the PCF8591P @ address 74
from smbus import SMBus
from time import sleep

# comment out the one that does not apply to your board
bus = SMBus(1) # for revision 2 boards
address = 74
control = 1<<6 # enable analog output

print(“Output a ramp on the D/A”)
print(“Ctrl C to stop”)

while True:
    for a in range(0,256):
        bus.write_byte_data(address, control, a) # output to D/A
        sleep(0.01)
