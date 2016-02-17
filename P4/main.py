#!/usr/bin/env python

"""
main.py -- Udacity conference server-side Python App Engine
    HTTP controller handlers for memcache & task queue access

$Id$

created by smallbarbary@gmail.com

"""

__author__ = 'smallbarbary@gmail.com (Yasser Albarbary)'

import webapp2
from google.appengine.api import app_identity
from google.appengine.api import mail
from google.appengine.api import memcache
from conference import ConferenceApi
from models import Speaker
from models import Session

MEMCACHE_FEATURED_SPEAKER = "FEATURED SPEAKER"
FEATURED_SPEAKER_TPL = ('Featured Speaker %s is presenting %s')

class SetAnnouncementHandler(webapp2.RequestHandler):
    def get(self):
        """Set Announcement in Memcache."""
        ConferenceApi._cacheAnnouncement()
        self.response.set_status(204)


class SendConfirmationEmailHandler(webapp2.RequestHandler):
    def post(self):
        """Send email confirming Conference creation."""
        mail.send_mail(
            'noreply@%s.appspotmail.com' % (
                app_identity.get_application_id()),     # from
            self.request.get('email'),                  # to
            'You created a new Conference!',            # subj
            'Hi, you have created a following '         # body
            'conference:\r\n\r\n%s' % self.request.get(
                'conferenceInfo')
        )

class CheckToSetFeaturedSpeaker(webapp2.RequestHandler):
    def post(self):
        """Check and Set as Featured Speaker if appropriate"""
        speaker = self.request.get('speakerId')
        # Gather all sessions by this speaker
        fsessions = Session.query(Session.speakerId==str(speaker))\
            .fetch(projection=[Session.name])
        #If more than 1 session, then make featured speaker
        if len(fsessions) > 1:
            # Lookup Speaker
            speaker = Speaker.get_by_id(int(speaker),)
            # Set the featured speaker and sessions in memcache
            announcement = FEATURED_SPEAKER_TPL % (speaker.displayName,
                ', '.join(session.name for session in fsessions))
            memcache.set(MEMCACHE_FEATURED_SPEAKER, announcement)

app = webapp2.WSGIApplication([
    ('/crons/set_announcement', SetAnnouncementHandler),
    ('/tasks/send_confirmation_email', SendConfirmationEmailHandler),
    ('/tasks/check_to_set_featured_speaker', CheckToSetFeaturedSpeaker),
], debug=True)
