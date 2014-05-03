#Fun with Raspberry Pi by Brian Bodiya & Tom Amlicke is licensed under a
#Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
#Based on a work at https://github.com/bodiya/funwithraspberrypi.
#
#Copyright Brian Bodiya & Tom Amlicke, 2014
#
import urllib2
import time

url = "http://api.thingspeak.com/channels/1417/field/1/last.txt"

seconds = 0
while seconds < 20:
  color = urllib2.urlopen(url).read()
  print("Latest color: " + color)
  seconds = seconds + 5
  time.sleep(5)
else:
  print "Done!"
