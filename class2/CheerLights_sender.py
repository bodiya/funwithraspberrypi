#Fun with Raspberry Pi by Brian Bodiya & Tom Amlicke is licensed under a
#Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
#Based on a work at https://github.com/bodiya/funwithraspberrypi.
#
#Copyright Brian Bodiya & Tom Amlicke, 2014
#
import sys
from twython import Twython
API_KEY = '***************YOUR DATA*****************'
API_SECRET = '***************YOUR DATA*****************'
ACCESS_TOKEN = '***************YOUR DATA*****************'
ACCESS_TOKEN_SECRET = '***************YOUR DATA*****************'

api = Twython(API_KEY,API_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET) 

api.update_status(status='@cheerlights My Pi wants %(color)s' % {"color": sys.argv[1]})
