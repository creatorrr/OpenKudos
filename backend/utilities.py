# -*- coding: utf-8 -*-
import os
import random
import logging

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

# Config Variables
import config

def getQuote():
    """Returns an awesome randomized quotation."""
    libraryFile=open('static/quotes.txt','r')
    library=libraryFile.readlines()
    return (random.choice(library)).split(';')

def parse_the_bloody(request):
    """This one prepares the signed url to shortlinks service."""
    
    # clean things up
    import urllib
    request = urllib.unquote(request)
    
    # divide and rule. ;)
    arguments = request.split('/')
    
    # dirty hack #1: stupid url-params extension
    while len(arguments) < 3:
        arguments.append('blah')
    
    # setting up the field
    ## TODO: As of this writing, We ain't filtering requests from idiots.
    ## Allowed actions: "incr", "decr", "newset", "stats"
    ## Beware: Dangerous stuff is coming through.
    options = {}
    
    options['action'] = arguments[0].lower()
    
    if options['action'] in ("decr", "incr", "stats"):
        set_id = arguments[1]
        options['set'] = set_id.split('-')[0]
        options['id'] = set_id.split('-')[1]
    
    elif options['action'] == "newset":
        options['set'] = arguments[1]
        options['secret'] = arguments[2]
    
    elif options['action'] == "flush":pass
    
    else:
        options['action'] = "blah"
    
        # just-in-case..
    for field in ('action', 'secret', 'set', 'id'):
        try:
            assert(options[field] is not None)
        except:
            options[field] = ''
    
    return options
    
def unpack(response):
    """This one unpacks the response."""
    
    import simplejson as json
    return json.loads(response)

def pack(result):
    """This one unpacks the result."""
    
    result_dict={}
    result_dict['data']=result
    import simplejson as json
    return "flyingpigscantfly(%s)" % json.dumps(result_dict)

def hitman(bullets = {}):
    """Render template and return it"""
    
    # template variables
    template_file = os.path.abspath('templates/index.html')
    template_fallback = os.path.abspath('templates/ohshit.html')

    quote=getQuote()

    vars = { 'quotation': quote[0],
             'quotation_author': quote[1],
             'quotation_link': quote[2],
             'title': 'Shrtnr',
             'analytics_id': config._GA_ID,
             }

    vars.update(bullets)                            # You don't mess with the hitman. (Just update the response)

    #try:
    return webapp.template.render(template_file, vars, debug=config._DEBUG)
    #except:
  #      logging.error('Webapp is an Ass. Couldn\'t even load a template.')
   # 	return webapp.template.render(template_fallback, vars, debug=config._DEBUG)
    
    
if __name__ == "__main__":
    print "STFU."               # You know people do this all the time.
