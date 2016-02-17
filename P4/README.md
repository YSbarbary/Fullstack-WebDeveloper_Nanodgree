# Conference Central (Modified)

App Engine application for the P4 Udacity training course.

## Online demo
https://even-antenna-96709.appspot.com/

## Requirements
- [App Engine][1]
- [Python][2]
- [Google Cloud Endpoints][3]

## What's Included
This is a modification of the Conference Central application provided by Udacity.
Included are:
- app.yaml (App Engine Base Configuration File)
- conference.py (Majority of Conference Central Code)
- cron.yaml (App Engine Cron Configuration File)
- index.yaml (App Engine DataStore index Configuration File)
- main.py (Functions to be run from CRON or Tasks)
- models.py (Data Models)
- README.md (This File)
- settings.py (Some Base Settings)
- utils.py
- static (Directory of Static Files)
- tempates (Directory of HTML template)

## Setup Instructions
1. Update the value of `application` in `app.yaml` to the app ID you
   have registered in the App Engine admin console and would like to use to host
   your instance of this sample.
1. Update the values at the top of `settings.py` to
   reflect the respective client IDs you have registered in the
   [Developer Console][4].
1. Update the value of CLIENT_ID in `static/js/app.js` to the Web client ID
1. (Optional) Mark the configuration files as unchanged as follows:
   `$ git update-index --assume-unchanged app.yaml settings.py static/js/app.js`
1. Run the app with the devserver using `dev_appserver.py DIR`, and ensure it's running by visiting your local server's address (by default [localhost:8080][5].)
1. (Optional) Generate your client library(ies) with [the endpoints tool][6].
1. Deploy your application.

## Modification/Additional Functionality Design Choices
1. Speakers
 - Option 1) Implemented this option.
Speaker is a (string) property of session.
If app business logic is not focusing on speakers 
(we are not keeping other information about the speaker other than name), 
faster implementation, faster read time for sessions and grabbing the speaker name. But duplicating speaker data (name).

Option 2) NOT Implemented this option. 
Speaker as a seperate entity. Use key (or keys) to associate with session. 
Can store more information about speakers. A single update to a speaker is reflected to every related session,
for example no need to iterate through every session object to fix a name typo for speaker.

2. Session - Session is defined as a new entity with a conference and Profile
as it's ancestor.  Sessions can contain multiple Speakers identified by their
numeric ID.  StartDateTime and EndDateTime are true DateTime fields and must be
addressed in the format YYYY-MM-DD HH:MM in 24hr **UTC** format.  The Session types
field can also contain multiple string values, in the future an ENUM would
be recommended similar to t-shirt size for data consistency.

3. WishList - The wishlist stores the key of sessions for the user with their
profile as it's ancestor for easy lookup.  As it is a wishlist, conference
registration is NOT required prior to use.

4. Featured Speaker - A memcache entry is created when creating a new session
and the speaker in question will have two or more sessions.  NOTE: this method
does not account for all situations, such as sessions in the past.

5. Querys - 3 Implemented
  1. **_getNextFiveSessions()_** - Returns the next five sessions to start, useful for
a day of event display.  Note this is not currently conference specific!
  2. **_deleteOldSessions()_** - Deletes sessions that have ended to save space, a more ideal
implementation might wait a period of time or instead archive them.  Designed to
be run from CRONs in final implementation.
  3. **non-workshop session before 7pm query problem** - Datastore only permits
  inequalities on a single field
per query, and by default this needs two (!=workshop >=19:00).  One possible
solution is to break this into two datastore querys (not ideal for large data)
in this case first filtering the session by time (only fetching the key and
  type info), and then remove the keys of all with the undesired type, then
  finally querying and returning the sessions from the remaining keys.  This is
  implemented in *sessionfilterByTypeAndTime()*.

##Attributions
This is based off the code provided by Udacity, and also examples from the
Google App Engine Documentation.

##History
Packaged by (yasser.al-barbary@live.com) for Udacity P4 project.

[1]: https://developers.google.com/appengine
[2]: http://python.org
[3]: https://developers.google.com/appengine/docs/python/endpoints/
[4]: https://console.developers.google.com/
[5]: https://localhost:8080/
[6]: https://developers.google.com/appengine/docs/python/endpoints/endpoints_tool
