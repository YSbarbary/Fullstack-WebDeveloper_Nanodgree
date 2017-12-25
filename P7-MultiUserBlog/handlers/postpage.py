# Models
from models.blog import Blog
from models.likes import Like
from models.unlikes import Unlike
from models.comment import Comment
from models.user import User

# Handlers

from handlers.bloghandler import Handler

from google.appengine.ext import db
from helpers import *
import time
# Define post page class-------------------------------------------------


class PostPage(Handler):
    @post_exists
    def get(self, blog_id):
        # get the key for the blog post
        key = db.Key.from_path("Blog", int(blog_id), parent=blog_key())
        post = db.get(key)

        # if the post does not exist throw a 404 error
        if not post:
            self.error(404)
            return
        # get likes, unlikes, comments for the blog post
        likes = Like.by_blog_id(post)
        unlikes = Unlike.by_blog_id(post)
        post_comments = Comment.all_by_blog_id(post)
        comments_count = Comment.count_by_blog_id(post)

        # render the page and show blog content, likes, unlikes, comments, etc.
        self.render(
            "post.html",
            post=post,
            likes=likes,
            unlikes=unlikes,
            comments_count=comments_count,
            post_comments=post_comments)

    @post_exists
    def post(self, blog_id):
        # get all the necessary parameters
        key = db.Key.from_path("Blog", int(blog_id), parent=blog_key())
        post = db.get(key)
        user_id = User.by_name(self.user.name)
        comments_count = Comment.count_by_blog_id(post)
        post_comments = Comment.all_by_blog_id(post)
        likes = Like.by_blog_id(post)
        unlikes = Unlike.by_blog_id(post)
        previously_liked = Like.check_like(post, user_id)
        previously_unliked = Unlike.check_unlike(post, user_id)

        # check if the user is logged in
        if self.user:
            # if the user clicks on like
            if self.request.get("like"):
                # check if the user try like his own post
                if post.user.key().id() != User.by_name(self.user
                                                            .name).key().id():
                    if previously_liked == 0:
                        # add like to the likes database and refresh the page
                        l = Like(
                            post=post, user=User.by_name(
                                self.user.name))
                        l.put()
                        time.sleep(0.1)
                        self.redirect('/post/%s' % str(post.key().id()))
                    # otherwise if the user has liked this post before throw
                    # and error
                    else:
                        error = "You have already liked this post"
                        self.render(
                            "post.html",
                            post=post,
                            likes=likes,
                            unlikes=unlikes,
                            error=error,
                            comments_count=comments_count,
                            post_comments=post_comments)
                # otherwise if the user is trying to like his own post throw an
                # error
                else:
                    error = "You cannot like your own posts"
                    self.render(
                        "post.html",
                        post=post,
                        likes=likes,
                        unlikes=unlikes,
                        error=error,
                        comments_count=comments_count,
                        post_comments=post_comments)
            # if the user clicks on unlike
            if self.request.get("unlike"):
                # first check if the user is trying to unlike his own post
                if post.user.key().id() != User.by_name(self.user
                                                            .name).key().id():
                    # then check if the user has unliked this post before
                    if previously_unliked == 0:
                        # add unlike to the unlikes database and refresh the
                        # page
                        ul = Unlike(
                            post=post, user=User.by_name(
                                self.user.name))
                        ul.put()
                        time.sleep(0.1)
                        self.redirect('/post/%s' % str(post.key().id()))
                    # otherwise if the user has unliked this post before throw
                    # and error
                    else:
                        error = "You have already unliked this post"
                        self.render(
                            "post.html",
                            post=post,
                            likes=likes,
                            unlikes=unlikes,
                            error=error,
                            comments_count=comments_count,
                            post_comments=post_comments)
                # otherwise if the user is trying to unlike his own post throw
                # an error
                else:
                    error = "You cannot unlike your own posts"
                    self.render(
                        "post.html",
                        post=post,
                        likes=likes,
                        unlikes=unlikes,
                        error=error,
                        comments_count=comments_count,
                        post_comments=post_comments)
            # if the user clicks on add comment get the comment text first
            if self.request.get("add_comment"):
                comment_text = self.request.get("comment_text")
                # check if there is anything entered in the comment text area
                if comment_text:
                    # add comment to the comments database and refresh page
                    c = Comment(
                        post=post, user=User.by_name(
                            self.user.name), text=comment_text)
                    c.put()
                    time.sleep(0.1)
                    self.redirect('/post/%s' % str(post.key().id()))
                # otherwise if nothing has been entered in the text area throw
                # an error
                else:
                    comment_error = "Please enter a comment in the text area"
                    self.render(
                        "post.html",
                        post=post,
                        likes=likes,
                        unlikes=unlikes,
                        comments_count=comments_count,
                        post_comments=post_comments,
                        comment_error=comment_error)
            # if the user clicks on edit post
            if self.request.get("edit"):
                # check if the user is the author of this post
                if post.user.key().id() == User.by_name(self.user
                                                            .name).key().id():
                    # take the user to edit post page
                    self.redirect('/edit/%s' % str(post.key().id()))
                # otherwise if the user is not the author of this post throw an
                # error
                else:
                    error = "You cannot edit other user's posts"
                    self.render(
                        "post.html",
                        post=post,
                        likes=likes,
                        unlikes=unlikes,
                        comments_count=comments_count,
                        post_comments=post_comments,
                        error=error)
            # if the user clicks on delete
            if self.request.get("delete"):
                # check if the user is the author of this post
                if post.user.key().id() == User.by_name(self.user
                                                            .name).key().id():
                    # delete the post and redirect to the main page
                    db.delete(key)
                    time.sleep(0.1)
                    self.redirect('/')
                # otherwise if the user is not the author of this post throw an
                # error
                else:
                    error = "You cannot delete other user's posts"
                    self.render(
                        "post.html",
                        post=post,
                        likes=likes,
                        unlikes=unlikes,
                        comments_count=comments_count,
                        post_comments=post_comments,
                        error=error)
        # otherwise if the user is not logged in take them to the login page
        else:
            self.redirect("/login")
