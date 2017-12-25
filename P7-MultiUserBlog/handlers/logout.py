# Handlers
from handlers.bloghandler import Handler

from helpers import *
# Define Logout Class-------------------------------------------------


class Logout(Handler):

    def get(self):
        # check is the user is logged in
        if self.user:
            # logout the user and take the user to the sign-up page
            self.logout()
            self.redirect("/signup")
        # otherwise if the user is not logged in take the user to the login
        # page and throw an error
        else:
            error = 'Please log in First.'
            self.render('login.html', error=error)
