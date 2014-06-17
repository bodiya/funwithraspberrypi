#Fun with Raspberry Pi by Brian Bodiya & Tom Amlicke is licensed under a
#Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
#Based on a work at https://github.com/bodiya/funwithraspberrypi.
#
#Copyright Brian Bodiya & Tom Amlicke, 2014
#
import sys
from twython import Twython
API_KEY = 'TUpqM3v2o7WREzQNi9ajQ7czt'
API_SECRET = 'Bq1WgztByKa51e20BzyMrF3bWkLuUr3EhBfTXruzgXMDrJViCS'
ACCESS_TOKEN ='2569910537-rGRuoO7S77A4PbnsLDhxPf91qCXcxjF3nNkdLFc'
ACCESS_TOKEN_SECRET = 'i6jZ3qDjd438bB7p6urCutaZdNc4m9MO5x6BNMtCmMD2c'

api = Twython(API_KEY,API_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET) 

api.update_status(status='@cheerlights My Pi wants %(color)s' % {"color": sys.argv[1]})
