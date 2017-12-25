# Models
from models.blog import Blog
from models.likes import Like

# Handlers

from handlers.postpage import PostPage

from google.appengine.ext import db
from helpers import *
import time


class LikePost(PostPage):

    def get(self, post_id):
        session_user_id = self.read_secure_cookie('user_id')
        l = Like.by_post_id(post_id)
        p_key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        p = db.get(p_key)
        for like in l:
            if like:
                if int(session_user_id) != int(p.key().id()):
                    if int(session_user_id) in like.post_user_id:
                        like.like_count -= 1
                        like.post_user_id.remove(int(session_user_id))
                        like.put()
                        time.sleep(0.2)
                        return self.redirect("/blog/%s" % post_id)
                    else:
                        like.like_count += 1
                        like.post_user_id.append(int(session_user_id))
                        like.put()
                        time.sleep(0.2)
                        return PostPage.get(self, post_id)

            else:
                error = "Error"
                return PostPage.get(self, post_id, error)
