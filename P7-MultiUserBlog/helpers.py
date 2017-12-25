import os
import re
import random
import hashlib
import hmac
from string import letters
import time
import webapp2
import jinja2
from functools import wraps

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
JINJA_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir),
    autoescape=True)

secret = 'uhf?6e7J44;JY{'




# Helping Functions definition 

def render_str(template, **params):
    t = JINJA_ENV.get_template(template)
    return t.render(params)

# set key for blog


def blog_key(name='default'):
    """define new relationship"""
    return db.Key.from_path('Blog', name)

# Define function to create secure cookie values


def make_secure_val(val):
    return '{}|{}'.format(val, hmac.new(secret, val).hexdigest())

# create a function to check secure cookie values


def check_secure_val(secure_val):
    """Check if the value is secure or Not"""
    val = secure_val.split('|')[0]
    if secure_val == make_secure_val(val):
        return val

# define function to make salt for making secure password


def make_salt(length=5):
    return ''.join(random.choice(letters) for x in xrange(length))

# define function to create password hashing  and salting


def make_pw_hash(name, pw, salt=None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(''.join([name, pw, salt])).hexdigest()
    return '%s,%s' % (salt, h)

# check if password is valid by hashing and comparing to existing hashed
# password


def valid_pw(name, password, h):
    salt = h.split(',')[0]
    return h == make_pw_hash(name, password, salt)

# get the key from User table


def users_key(group='default'):
    return db.Key.from_path('users', group)

# define what a valid username is
USER_RE = re.compile(r'^[a-zA-Z0-9_-]{3,20}$')


def valid_username(username):
    return username and USER_RE.match(username)

# define what a valid password is
PASS_RE = re.compile(r'^.{3,20}$')


def valid_password(password):
    return password and USER_RE.match(password)



# Decorators
def post_exists(function):
    @wraps(function)
    def wrapper(self, post_id, *args, **kwargs):
        key = db.Key.from_path('Blog', int(post_id), parent=blog_key())
        post = db.get(key)
        if not post:
            return self.error("404")
        else:
            return function(self, post_id, *args, **kwargs)
    return wrapper
    
    
def user_logged_in(function):
    @wraps(function)
    def wrapper(self, *args, **kwargs):
        if not self.user:
            return self.redirect("/login")
        else:
            return function(self, *args, **kwargs)
    return wrapper



