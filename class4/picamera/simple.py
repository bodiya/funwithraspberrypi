#Fun with Raspberry Pi by Brian Bodiya & Tom Amlicke is licensed under a
#Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
#Based on a work at https://github.com/bodiya/funwithraspberrypi.
#
#Copyright Brian Bodiya & Tom Amlicke, 2014
#

import time
import picamera

camera = picamera.PiCamera()

try:
    camera.hflip = True
    camera.vflip = True
    camera.start_preview()
    time.sleep(2)
    camera.capture('photo.jpg')
    camera.stop_preview()
finally:
    camera.close()

