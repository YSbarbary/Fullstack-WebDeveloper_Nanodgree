# Handlers

from handlers.bloghandler import Handler


from helpers import *
# Define main Page Class-------------------------------------------------


class MainPage(Handler):

    def get(self):
        # get all blog posts ordered Descending by creation date
        blogs = db.GqlQuery("SELECT * FROM Blog ORDER BY created DESC")
        # if there are any existing blog posts render the page with those posts
        if blogs:
            self.render("blogs.html", blogs=blogs)

