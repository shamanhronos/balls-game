import math

from object import Object

class Ball(Object):

	def __init__(self, game, pos, radius, color):
		self.game = game
		self.pos = pos
		self.radius = radius
		self.color = color

	def distance(self, pos):
		return math.sqrt((self.pos[0]-pos[0])**2 + (self.pos[1]-pos[1])**2)

	def collision(self):
		objects_ = list(self.game.objects)
		objects_.remove(self)
		if len(objects_) == 0:
			return None

		min_distance = self.distance(objects_[0].pos)
		min_distance_obj = objects_[0]
		for obj in objects_:
			d = self.distance(obj.pos)
			if d < min_distance:
				min_distance = d
				min_distance_obj = obj
		
		if min_distance <= 2 * self.radius:
			return min_distance_obj

	def collision_with_coordinates(self, pos):
		distance = self.distance(pos)
		return distance <= self.radius