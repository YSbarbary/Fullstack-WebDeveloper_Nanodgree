from google.appengine.ext import db
from helpers import *
from user import User
from blog import Blog
# define unlike class-------------------------------------------------

# store unlikes to datatbase
class Unlike(db.Model):
    post = db.ReferenceProperty(Blog, required=True)
    user = db.ReferenceProperty(User, required=True)

    # get number of unlikes for a blog
    @classmethod
    def by_blog_id(cls, blog_id):
        ul = Unlike.all().filter('post =', blog_id)
        return ul.count()

    # get number of unlikes for a blog and user id
    @classmethod
    def check_unlike(cls, blog_id, user_id):
        cul = Unlike.all().filter(
            'post =', blog_id).filter(
            'user =', user_id)
        return cul.count()
