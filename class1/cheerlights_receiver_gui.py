#Fun with Raspberry Pi by Brian Bodiya & Tom Amlicke is licensed under a
#Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
#Based on a work at https://github.com/bodiya/funwithraspberrypi.
#
#Copyright Brian Bodiya & Tom Amlicke, 2014
#
import urllib2
from Tkinter import *

url = "http://api.thingspeak.com/channels/1417/field/1/last.txt"

root = Tk()
root.geometry("200x200")
root.title("Cheerlights Receiver")

def update_color():
  color = urllib2.urlopen(url).read()
  print("Latest color: " + color)
  root.configure(background=color)
  root.after(1000,update_color)
root.after(1000,update_color)

root.mainloop()
