OpenKudos
---------------------

OpenKudos - An open source port of the "kudos" button as seen on http://dcurt.is!


##Description:

An App Engine based kudos server.

###Why?
* Kudos concept (as seen on dcurt.is) is cool.
* I wanted to use it.

How-To
----------

Just clone into this git repository, edit app.yaml and config.py and deploy to appengine!

Enjoy
----------

Feedback, improvements and critique are greatly appreciated. **Fork away!**
You can write me an email: *singh@diwank.name*

Specs
-----

###App Details:

@ platform: App Engine   
@ actions:   

- /incr/set-id              # increment existing set-id or create new id
- /decr/set-id              # decrement existing set-id (dont create new id)
- /newset/name/secret       # create new set (if secret is okay)
- /backup                   # backup stats to datastore (accessed via cron)
- /stats/set-id             # Return stats for set-id (return 0 if does not exist)
- /                         # Print all stats

Ideas
-----

Some ideas for future improvements:

* Use cookies to mark people off.


