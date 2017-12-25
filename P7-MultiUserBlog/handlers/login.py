
# Models
from models.user import User

# Handlers

from handlers.bloghandler import Handler

from helpers import *

# Define Login Class-------------------------------------------------


class Login(Handler):

    def get(self):
        self.render('login.html')

    def post(self):
        # get the username and password entered by the user
        username = self.request.get('username')
        password = self.request.get('password')

        # get the user account associated with that username and password
        u = User.login(username, password)

        # if there is a user account associated with that username and password
        if u:
            # login and redirect to the welcome page
            self.login(u)
            self.redirect('/greeting')
        # otherwise if there isn't a user account associated with that username
        # and password throw an error
        else:
            error = 'Invalid login'
            self.render('login.html', error=error)
