#Fun with Raspberry Pi by Brian Bodiya & Tom Amlicke is licensed under a
#Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
#Based on a work at https://github.com/bodiya/funwithraspberrypi.
#
#Copyright Brian Bodiya & Tom Amlicke, 2014
#

import picamera

with picamera.PiCamera() as camera:
    camera.start_preview()
    try:
        for i in range(10):
            camera.hflip = True
            camera.vflip = True            
            # TODO: Choose a different parameter to change in your test sheet
            camera.brightness = i*10
            camera.capture('sheet%03i.jpg' % i)
            # TODO: Tk to show the image in a dialog box
    finally:
        camera.stop_preview()
        camera.close()
