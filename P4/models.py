#!/usr/bin/env python

"""models.py

Udacity conference server-side Python App Engine data & ProtoRPC models

$Id: models.py

"""

__author__ = 'yasser.al-barbary@live.com (Yasser Albarbary)'

import httplib
import endpoints
from protorpc import messages
from google.appengine.ext import ndb

class ConflictException(endpoints.ServiceException):
    """ConflictException -- exception mapped to HTTP 409 response"""
    http_status = httplib.CONFLICT

class Profile(ndb.Model):
    """Profile -- User profile object"""
    displayName = ndb.StringProperty()
    mainEmail = ndb.StringProperty()
    teeShirtSize = ndb.StringProperty(default='NOT_SPECIFIED')
    conferenceKeysToAttend = ndb.StringProperty(repeated=True)

class ProfileMiniForm(messages.Message):
    """ProfileMiniForm -- update Profile form message"""
    displayName = messages.StringField(1)
    teeShirtSize = messages.EnumField('TeeShirtSize', 2)

class ProfileForm(messages.Message):
    """ProfileForm -- Profile outbound form message"""
    displayName = messages.StringField(1)
    mainEmail = messages.StringField(2)
    teeShirtSize = messages.EnumField('TeeShirtSize', 3)
    conferenceKeysToAttend = messages.StringField(4, repeated=True)

class StringMessage(messages.Message):
    """StringMessage-- outbound (single) string message"""
    data = messages.StringField(1, required=True)

class BooleanMessage(messages.Message):
    """BooleanMessage-- outbound Boolean value message"""
    data = messages.BooleanField(1)

class Conference(ndb.Model):
    """Conference -- Conference object"""
    name            = ndb.StringProperty(required=True)
    description     = ndb.StringProperty()
    organizerUserId = ndb.StringProperty()
    topics          = ndb.StringProperty(repeated=True)
    city            = ndb.StringProperty()
    startDate       = ndb.DateProperty()
    month           = ndb.IntegerProperty() # TODO: do we need for indexing like Java?
    endDate         = ndb.DateProperty()
    maxAttendees    = ndb.IntegerProperty()
    seatsAvailable  = ndb.IntegerProperty()

class ConferenceForm(messages.Message):
    """ConferenceForm -- Conference outbound form message"""
    name            = messages.StringField(1)
    description     = messages.StringField(2)
    organizerUserId = messages.StringField(3)
    topics          = messages.StringField(4, repeated=True)
    city            = messages.StringField(5)
    startDate       = messages.StringField(6) #DateTimeField()
    month           = messages.IntegerField(7)
    maxAttendees    = messages.IntegerField(8)
    seatsAvailable  = messages.IntegerField(9)
    endDate         = messages.StringField(10) #DateTimeField()
    websafeSessionKey      = messages.StringField(11)
    organizerDisplayName = messages.StringField(12)

class ConferenceForms(messages.Message):
    """ConferenceForms -- multiple Conference outbound form message"""
    items = messages.MessageField(ConferenceForm, 1, repeated=True)

class TeeShirtSize(messages.Enum):
    """TeeShirtSize -- t-shirt size enumeration value"""
    NOT_SPECIFIED = 1
    XS_M = 2
    XS_W = 3
    S_M = 4
    S_W = 5
    M_M = 6
    M_W = 7
    L_M = 8
    L_W = 9
    XL_M = 10
    XL_W = 11
    XXL_M = 12
    XXL_W = 13
    XXXL_M = 14
    XXXL_W = 15

class ConferenceQueryForm(messages.Message):
    """ConferenceQueryForm -- Conference query inbound form message"""
    field = messages.StringField(1)
    operator = messages.StringField(2)
    value = messages.StringField(3)

class ConferenceQueryForms(messages.Message):
    """ConferenceQueryForms -- multiple ConferenceQueryForm inbound form message"""
    filters = messages.MessageField(ConferenceQueryForm, 1, repeated=True)

class Session(ndb.Model):
    """Session -- Session object"""
    name            = ndb.StringProperty(required=True)
    highlights      = ndb.StringProperty()
    location        = ndb.StringProperty()
    speakerId       = ndb.StringProperty(repeated=True)
    types           = ndb.StringProperty(repeated=True)
    startDateTime   = ndb.DateTimeProperty()
    endDateTime     = ndb.DateTimeProperty()

class SessionForm(messages.Message):
    """SessionForm -- Session outbound form message"""
    name            = messages.StringField(1, required=True)
    highlights      = messages.StringField(2)
    location        = messages.StringField(3)
    speakerId       = messages.StringField(4, repeated=True)
    types           = messages.StringField(5, repeated=True)
    startDateTime   = messages.StringField(6) #DateTimeField()
    endDateTime     = messages.StringField(7) #DateTimeField()
    websafeSessionKey      = messages.StringField(8)

class SessionForms(messages.Message):
    """SessionForms -- multiple Session outbound form message"""
    items = messages.MessageField(SessionForm, 1, repeated=True)

class Speaker(ndb.Model):
    """Speaker -- Speaker object"""
    displayName     = ndb.StringProperty(required=True)
    title           = ndb.StringProperty()
    mainEmail       = ndb.StringProperty()

class SpeakerForm(messages.Message):
    """SpeakerForm -- Speaker outbound form message"""
    displayName     = messages.StringField(1, required=True)
    title           = messages.StringField(2)
    mainEmail       = messages.StringField(3)
    websafeSessionKey      = messages.StringField(4)

class SpeakerMiniForm(messages.Message):
    """SpeakerForm -- Speaker outbound form message"""
    displayName     = messages.StringField(1, required=True)

class WishList(ndb.Model):
    """WishList -- WishList object"""
    SessionKey       = ndb.KeyProperty(required=True, kind='Session')

class WishListForm(messages.Message):
    """WishListForm -- update WishList form message"""
    SessionKey       = messages.StringField(1)
