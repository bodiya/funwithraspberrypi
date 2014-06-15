#Fun with Raspberry Pi by Brian Bodiya & Tom Amlicke is licensed under a
#Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
#This example based on a work at:
#https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/software.
#
#Copyright Brian Bodiya & Tom Amlicke, 2014
#
import os
import glob
import time
import httplib, urllib

os.system('modprobe w1-gpio pullup=1')
os.system('modprobe w1-therm strong_pullup=1')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
apikey='INSERT_WRITE_API_KEY_HERE'

def read_temp_raw():
  f = open(device_file, 'r')
  lines = f.readlines()
  f.close()
  return lines

def read_temp():
  lines = read_temp_raw()
  while lines[0].strip()[-3:] != 'YES':
    time.sleep(0.2)
    lines = read_temp_raw()
  equals_pos = lines[1].find('t=')
  if equals_pos == -1:
    return "Error reading temperator"
  temp_string = lines[1][equals_pos+2:]
  temp_c = float(temp_string) / 1000.0
  temp_f = temp_c * 9.0 / 5.0 + 32.0
  return temp_f

def post_temp(deg_f):
  print "Updating Thingspeak with:", deg_f
  params = urllib.urlencode({'field1':deg_f,'key':apikey})
  headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
  conn = httplib.HTTPConnection("api.thingspeak.com:80")
  conn.request("POST", "/update", params, headers)
  ts_response = conn.getresponse()
  print "Thingspeak Response:", ts_response.status, ts_response.reason
  conn.close

while True:
  try:
    latest_temp = read_temp()
    if isinstance(latest_temp, float):
      post_temp(latest_temp)
    time.sleep(20)
  except KeyboardInterrupt:
    exit()
  except:
    e = sys.exc_info()[0]
    print "Error:\n%s" % e
    print "Aborting\n"
    exit()
 
