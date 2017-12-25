# Models
from models.user import User

# Handlers
from handlers.signup import Signup

from helpers import *


# Define register class-------------------------------------------------


class Register(Signup):
    """Helper class for Signup process"""
    def done(self):
        # check if the username already exists
        u = User.by_name(self.username)
        # if the username already exists throw an error
        if u:
            error_message = 'That user already exists.'
            self.render('signup.html', error_username=error_message)
        # otherwise if the username doesn't exist yet add the user, login the
        # redirect to greeting page
        else:
            u = User.register(self.username, self.password, self.email)
            u.put()

            self.login(u)
            self.redirect('/greeting')

