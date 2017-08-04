class Movie():
	'''
	Each instance of class Movie stores a single film
	with 4 prperties:
		title : File title
		storyline : One sentence film pitch
		poster_image_url : URL of the film poster
		trailer_youtube_url : Link to film trailer on youtube
	'''

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

