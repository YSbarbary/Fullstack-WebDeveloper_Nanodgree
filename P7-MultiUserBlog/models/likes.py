from google.appengine.ext import db
from helpers import *
from user import User
from blog import Blog

# Define likes Class-------------------------------------------------

# store likes in database


class Like(db.Model):
    post = db.ReferenceProperty(Blog, required=True)
    user = db.ReferenceProperty(User, required=True)

    # get number of likes
    @classmethod
    def by_blog_id(cls, blog_id):
        l = Like.all().filter('post =', blog_id)
        return l.count()

    # get number of likes for a blog and user id
    @classmethod
    def check_like(cls, blog_id, user_id):
        cl = Like.all().filter(
            'post =', blog_id).filter(
            'user =', user_id)
        return cl.count()
