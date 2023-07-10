from ball import Ball

class Player(Ball):

	def __init__(self, game, pos, radius, color):
		self.game = game
		self.pos = pos
		self.radius = radius
		self.color = color