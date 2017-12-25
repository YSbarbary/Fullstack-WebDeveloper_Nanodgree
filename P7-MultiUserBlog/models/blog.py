from google.appengine.ext import db
from helpers import *
from user import User

# Define class Blog -------------------------------------------------

# save blogs posts to database


# Define class Blog -------------------------------------------------

# save blogs posts to database


class Blog(db.Model):
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    user = db.ReferenceProperty(User,
                                required=True,
                                collection_name="blogs")

    def render(self):
        self._render_text = self.content.replace('\n', '<br>')
        return render_str("post.html", post=self)
