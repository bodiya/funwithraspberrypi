#Fun with Raspberry Pi by Brian Bodiya & Tom Amlicke is licensed under a
#Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
#Based on a work at https://github.com/bodiya/funwithraspberrypi.
#
#Copyright Brian Bodiya & Tom Amlicke, 2014
#
import RPi.GPIO as GPIO
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

try:
  for current_color in colors:
    print("Current color: " + current_color)
    pwmRed.ChangeDutyCycle(colors[current_color][0])
    pwmGreen.ChangeDutyCycle(colors[current_color][1])
    pwmBlue.ChangeDutyCycle(colors[current_color][2])
    time.sleep(5)
  GPIO.cleanup()
except KeyboardInterrupt:
  GPIO.cleanup()
