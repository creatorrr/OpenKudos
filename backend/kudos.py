# -*- coding: utf-8 -*-

""" Explanation of App in pseudo-code:
    App:
        (for) Request = /
            - Push All Stats
            - As webpage
        (for) Request = /incr(decr)/set-id
            - increment set:id
            - Push Stats
            - As text
        (for) Request = /newset/name/secret
            - Push Result
            - As text
        (for) Request = /stats/set-id
            - Push Stats
            - As text

"""

import config
from utilities import *
from models import *
from google.appengine.api import memcache

Data = Model()                           # Data Access Layer

class Kudos(object):
    def __init__(self, options):

        self.action = options['action']
        self.set = options['set']
        self.id = options['id']
        self.secret = options['secret']

    def incr(self):
        """Adds Kudos."""
        
        try:
            memcache.incr(key = "%s:%s" % (self.set, self.id), initial_value = 0)
            # Data Store Write
            Data.incr_kudos(self.set, self.id)
            return True
        except:
            return False

    def decr(self):
        """Subtract Kudos."""
        
        try:
            memcache.decr(key = "%s:%s" % (self.set, self.id), initial_value = 1)
            # Data Store Write
            Data.incr_kudos(self.set, self.id, score = -1)
            return True
        except:
            return False

    def stats(self):
        """Gets Kudos."""
        
        kudos = memcache.get(key = "%s:%s" % (self.set, self.id))
        if kudos is not None:
            return kudos
        else:# Data Store Fetch
            return Data.get_kudos(self.set, self.id)

    def newset(self):
        """Adds set."""
        
        if self.secret == config._SECRET:
            try:
                Data.add_set(self.set)
                return True
            except:
                return False
        else:# Data Store Fetch
            return False

    def blah(self):
        """Gets all stats."""
        
        values = Data.get_all()
        
        values_library = {}                   # storing bookmarks in a dictionary as key-value pairs
        for value in values:
            values_library[value.group.name+':'+value.name] = value.kudos

        return values_library

    def respond(self):
        """The big bully of the class."""
        
        response = {}
        response.update(action = self.action)
        
        # Good ol' switch - case

        if self.action == "incr":
            self.incr()
            response.update(result = self.stats(), type = "text")
        
        elif self.action == "decr":
            self.decr()
            response.update(result = self.stats(), type = "text")
                    
        elif self.action == "stats":
            response.update(result = self.stats(), type = "text")
                            
        elif self.action == "newset":
            response.update(result = str(self.newset()), type = "text")
        
        elif self.action == "blah":
            all_stats = self.blah()
            response.update(stats = all_stats, type = "page")
        
        else: pass                          # Who cares?
        
        return response

if __name__ == "__main__":
    print "STFU."               # You know people do this all the time.
