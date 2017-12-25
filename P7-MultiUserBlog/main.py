import os
import re
import random
import hashlib
import hmac
from string import letters
import time

import webapp2
import jinja2
from google.appengine.ext import db


# Models

from models.user import User
from models.blog import Blog
from models.likes import Like
from models.unlikes import Unlike
from models.comment import Comment

# Handlers

from handlers.greeting import Greeting
from handlers.deletecomment import DeleteComment
from handlers.editcomment import EditComment
from handlers.editpost import EditPost
from handlers.like import LikePost
from handlers.login import Login
from handlers.logout import Logout
from handlers.mainpage import MainPage
from handlers.newpost import NewPost
from handlers.postpage import PostPage
from handlers.register import Register

from helpers import *

# Define Routes


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/newpost', NewPost),
    ('/post/([0-9]+)', PostPage),
    ('/login', Login),
    ('/logout', Logout),
    ('/signup', Register),
    ('/greeting', Greeting),
    ('/edit/([0-9]+)', EditPost),
    ('/blog/([0-9]+)/like', LikePost ),
    ('/blog/([0-9]+)/editcomment/([0-9]+)', EditComment),
    ('/blog/([0-9]+)/deletecomment/([0-9]+)', DeleteComment),
], debug=True)
