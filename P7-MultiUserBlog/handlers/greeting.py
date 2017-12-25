# Models
from models.blog import Blog

# Handlers
from handlers.bloghandler import Handler

from helpers import *

# Define greeting class -------------------------------

class Greeting(Handler):

    def get(self):
        # check is the user is logged in
        if self.user:
            # show the greeting message 
            self.render("greeting.html", username=self.user.name)
        # otherwise if the user is not logged in go to login from
        # page
        else:
            self.redirect("/login")
            