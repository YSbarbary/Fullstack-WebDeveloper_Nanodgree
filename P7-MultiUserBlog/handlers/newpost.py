# Models
from models.blog import Blog
from models.likes import Like
from models.unlikes import Unlike
from models.user import User

from handlers.bloghandler import Handler
import time


from helpers import *
# Define new post class-------------------------------------------------


class NewPost(Handler):
    @user_logged_in
    def get(self):
        # if user is logged in take us to newpost page
        if self.user:
            self.render("newpost.html")
        # otherwise take us to login page
        else:
            self.redirect("/login")

    @user_logged_in
    def post(self):
        if self.user:
            # get the subject, content of the post and username of the user
            subject = self.request.get("subject")
            content = self.request.get("content").replace('\n', '<br>')
            user_id = User.by_name(self.user.name)
            # if we have a subject and content of the post add it to the
            # database and redirect us to the post page
            if subject and content:
                a = Blog(
                    parent=blog_key(),
                    subject=subject,
                    content=content,
                    user=user_id)
                a.put()
                return self.redirect('/post/%s' % str(a.key().id()))

            # othersie throw and error to let the user know that both subject
            # and content are required
            else:
                post_error = "Please enter a subject and the blog content"
                self.render(
                    "newpost.html",
                    subject=subject,
                    content=content,
                    post_error=post_error)
        else:
            self.redirect("/login")
