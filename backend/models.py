""" Data Models:
        * Set
            - Name
        * ID
            - Name
            - Kudos

"""

from google.appengine.ext import db

class Set(db.Model):
    name = db.StringProperty()

class ID(db.Model):
    name = db.StringProperty()
    group = db.ReferenceProperty()
    kudos = db.IntegerProperty()

class Model(object):
    def __init__(self):
        """Initialize Database if first run"""
        
        query = Set.all()
        result = query.fetch(1)
        if not result:
            new_set = Set(name = "Set1",
                          key_name = "Set1"
                          )
            new_set.put()
        
    def add_set(self, set_name):
        """Flying pigs can't add sets to your database."""        
        
        try:
            new_set = Set(name = set_name,
                          key_name = set_name
                          )
            new_set.put()
            
            return True
        except:
            return False

                
    def incr_kudos(self, set_name, id_string, score = 1):
        """Increment Kudos with score. Defaults to +1"""
        
        key = db.Key.from_path('Set', set_name,
                                'ID', id_string
                               )
        try:
            value = db.get(key)
        except:
            return self.add_id(set_name, id_string)
        
        value.kudos = value.kudos + score
        value.put()
        return True
    
    def add_id(self, set_name, id_string):
        """Add new id."""
        
        set_key = db.Key.from_path('Set', set_name)
        if not db.get(set_key):
            return False
        
        new_id = ID(name = id_string, kudos = 1, group = set_key,
                    parent = set_key,
                    key_name = id_string)
        try:
            new_id.put()
            return True
        except:
            return False
        
    def get_kudos(self, set_name, id_string):
        """I passed with flying colors. Kudos!"""
        
        key = db.Key.from_path('Set', set_name,
                                'ID', id_string
                               )
        try:
            value = db.get(key)
            kudos = value.kudos
            return kudos
        except:
            return False

            
    def get_all(self, max_entries = 1000, begin = 0):
        """Fetches all stats."""
        
        query = ID.all()
        try:
            result = query.fetch(limit = max_entries, offset = begin)
            return result
        except:
            return None


if __name__ == "__main__":
    print "STFU."                        # You know people do this all the time.
