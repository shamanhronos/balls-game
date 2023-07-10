import math

class Object:

	def __init__(self, game, pos, color):
		self.game = game
		self.pos = pos
		self.color = color

	def angle(self, object):
		delta_x = object.pos[0] - self.pos[0]
		delta_y = object.pos[1] - self.pos[1]
		return math.atan2(delta_y, delta_x);