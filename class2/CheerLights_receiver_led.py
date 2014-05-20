#Fun with Raspberry Pi by Brian Bodiya & Tom Amlicke is licensed under a
#Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
#Based on a work at https://github.com/bodiya/funwithraspberrypi.
#
#Copyright Brian Bodiya & Tom Amlicke, 2014
#
import RPi.GPIO as GPIO
import urllib2
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

pwmRed = GPIO.PWM(22, 500)
pwmRed.start(100)

pwmGreen = GPIO.PWM(27, 500)
pwmGreen.start(100)

pwmBlue = GPIO.PWM(17, 500)
pwmBlue.start(100)

colors = {'red': [100,0,0],
          'green': [0,100,0],
          'blue': [0,0,100],
          'cyan': [0,100,100],
          'white': [100,100,100],
          'warmwhite': [99,96,90],
          'purple': [50,0,50],
          'magenta': [100,0,100],
          'yellow': [100,100,0],
          'orange': [100,65,0],
          'pink': [100,75,80],
          'oldlace': [99,96,90]}

url = "http://api.thingspeak.com/channels/1417/field/1/last.txt"

try:
  while 1:
    last_color = urllib2.urlopen(url).read()
    print("Latest color: " + last_color)
	pwmRed.ChangeDutyCycle(colors[last_color][0])
	pwmGreen.ChangeDutyCycle(colors[last_color][1])
	pwmBlue.ChangeDutyCycle(colors[last_color][2])
	time.sleep(5)
except KeyboardInterrupt:
  GPIO.cleanup()
