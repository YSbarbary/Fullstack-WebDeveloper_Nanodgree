# This class Moive provides the format for our movie trailers website.
# Each movie will feature a title, poster image,
# Youtube trailer, and storyline.
import webbrowser


class Movie():
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 movie_directors,
                 movie_writer,
                 movie_stars,
                 movie_rating,
                 poster_image,
                 trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.directors = movie_directors
		self.writer = movie_writer
		self.stars = movie_stars
		self.rating = movie_rating
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
