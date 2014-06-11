#Fun with Raspberry Pi by Brian Bodiya & Tom Amlicke is licensed under a
#Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
#Based on a work at https://github.com/bodiya/funwithraspberrypi.
#
#Copyright Brian Bodiya & Tom Amlicke, 2014
#
import sys
from twython import Twython
import random

API_KEY = '***************YOUR DATA*****************'
API_SECRET = '***************YOUR DATA*****************'
ACCESS_TOKEN = '***************YOUR DATA*****************'
ACCESS_TOKEN_SECRET = '***************YOUR DATA*****************'

colors = {'r': 'red',
          'g': 'green',
          'b': 'blue',
          'c': 'cyan',
          'w': 'white',
          'p': 'purple',
          'm': 'magenta',
          'y': 'yellow',
          'o': 'orange'}


verbs = ['demands','requests','would like','desires','pines for']
adjectives = ['beautiful','awesome','pretty','gross','evil','aweful']

api = Twython(API_KEY,API_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET) 

while 1:
  try:
    char_input = raw_input("Please input one of [r,g,b,c,w,p,m,y,o]:")
    color = colors[char_input]
    verb = verbs[random.randrange(0,len(verbs))]
    adjective = adjectives[random.randrange(0,len(adjectives))]
    new_status = '@cheerlights My Pi %(verb)s the %(adjective)s color %(color)s' % \
                 {"color"     : color,
                  "verb"      : verb,
                  "adjective" : adjective}
    print "Updating status to:\n%s" % new_status
    api.update_status(status=new_status)
    print "Color successfully changed to %s" % color
  except KeyError:
    print "That's not a valid color!"
  except KeyboardInterrupt:
    sys.exit(0)
  except:
    e = sys.exc_info()[0]
    print "Error:\n%s" % e

