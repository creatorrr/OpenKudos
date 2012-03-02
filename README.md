# OpenKudos

**OpenKudos** - _An open source port of the awesome "kudos" button as seen on http://dcurt.is!_

* * *

## Description

### What?
* An open source port of Dustin Curtis' Kudos Buttons
* Cooler upvote buttons for anything.

### Why?
* Kudos button is so damn cool.
* I just had to use it! :D

### How?
* Server runs on Google App Engine Goodness!!!
* IFrame based async updates.

* * *

## Instructions

### Backend
* Just clone into this git repository.
* Edit app.yaml and config.py
* Deploy to appengine!
* Run http://your-kudos-app-id.appspot.com/newset/SetName/YourSecret to create a new set named SetName where YourSecret is the secret you set in config.py

### Frontend
* Include kudos.css and kudos.css
* Copy and paste button snippet from kudos.html
* Replace a[href] with http://your-kudos-app-id.appspot.com/incr/SetName-IDName
* That's it (Yay!)

* * *

## Specs

### Backend

@ platform: App Engine   
@ actions:   

- /incr/set-id              # increment existing set-id or create new id
- /decr/set-id              # decrement existing set-id or create new id
- /newset/name/secret       # create new set (if secret is okay)
- /stats/set-id             # Return stats for set-id
- /                         # Print all stats

Note: id's are _alpahnumeric_

### Frontend

@ technologies:

- jQuery
- HTML5
- CSS3 Animations

@ implementation

- async behaviour implemented using IFrames.

* * *

## Enjoy

This is a fun project.   
Feedback, improvements and critique are greatly appreciated.   
You can write to me at: *singh@diwank.name*   


### Examples

#### A List of My Ideas
* **Used here** http://idea.diwank.name
* **Backend** http://kudos.diwank.name

#### My Blag
* **Used here** http://blag.diwank.name/Startups/About-YC
* **Backend** http://kudos.diwank.name

* * *

## Ideas


Some ideas for improvements:

* Use cookies to mark people off.
* Make automated backups of memcache.
* Use JSONP instead of IFrames.

* * *

## License

Copyright (c) 2012 Diwank Singh Tomer

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
