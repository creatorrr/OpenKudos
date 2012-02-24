# -*- coding: utf-8 -*-

# environment vars
import os

import logging

# webapp utilities
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

# import project modules
import config
from utilities import *
from kudos import *

class Handler(webapp.RequestHandler):
  """For app requests."""

  def get(self, request):
    """Callback for GET requests.
            Args:
             - request: the request. [Sigh.]
    """
    
    options = parse_the_bloody(request)         # Does what it says.
    server = Kudos(options)
    
    response = server.respond()
    logging.info('Some bloke tried to initiate a ' + server.action)
    
    if response['return_type'] == 'text':
        self.response.headers['Content-Type'] = 'text/text'
        result = response['result']
    
    elif response['return_type'] == 'html':
        self.response.headers['Content-Type'] = 'text/html'
        result = hitman(response)     # Renders template. No bloodshed.
    
    self.response.out.write(result)           # Flush response to her
    return


# Map url's to handlers
urls = [
    (r'/(.*)', Handler), # handles actions
]

application = webapp.WSGIApplication(urls, debug=config._DEBUG)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
