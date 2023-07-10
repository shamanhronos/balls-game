import pygame
import math
import time
import random

from ball import Ball
from player import Player

class Game:

	objects = []

	def __init__(self):

		pygame.init()

		number_balls = 0
		width = 800
		height = 600
		dis = pygame.display.set_mode((width, height))
		clock = pygame.time.Clock()
		
		p = None
		#p = Player(self, [width/2, height/2], 40, "green")
		#self.objects.append(p)
		self.objects.append(Ball(self, [width/2, height/2], 200, "green"))

		font = pygame.freetype.SysFont("Hack", 24)

		mouse_pos = (width/2, height/2)
		
		game_over = False
		spawned = False
		start_time = int(time.time())
		while not game_over:
			seconds = int(time.time()) - start_time
			
			click_pos = None
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					game_over = True
				elif event.type == pygame.MOUSEMOTION:
					mouse_pos = event.pos
				elif event.type == pygame.MOUSEBUTTONDOWN:
					click_pos = event.pos
					
			dis.fill((240, 240, 240))

			if p != None:
				p.pos[0] = p.pos[0] + (mouse_pos[0] - p.pos[0]) * 0.15
				p.pos[1] = p.pos[1] + (mouse_pos[1] - p.pos[1]) * 0.15

				collidedWith = p.collision()
				if collidedWith != None:
					if type(collidedWith) == Ball:
						self.objects.remove(collidedWith)

			for i in range(0, len(self.objects)):
				obj = self.objects[i]
				if type(obj) != Ball:
					continue
				
				collidedWith = obj.collision()
				if collidedWith != None:
					angle = collidedWith.angle(obj)
					speed = 3
					obj.pos[0] = obj.pos[0] + speed * math.cos(angle)
					obj.pos[1] = obj.pos[1] + speed * math.sin(angle)

			if click_pos != None:
				for i in range(0, len(self.objects)):
					obj = self.objects[i]
					if type(obj) == Player or type(obj) == Ball:
						if obj.collision_with_coordinates(click_pos):
							if obj == p:
								p = None
							number_balls = number_balls + 1
							self.objects.remove(obj)
							colors = ["red", "blue", "yellow", "gray", "black", "pink", "purple", "turquoise", "orange"]
							color = random.choice(colors)
							self.objects.append(Ball(self, [random.randint(0,width), random.randint(0,height)], random.randint(10,100), color))
							break

			for obj in self.objects:
				pygame.draw.circle(dis, obj.color, obj.pos, obj.radius)
			font.render_to(dis, (8, 8), "time:"+str(seconds)+"s", pygame.Color("black"))
			font.render_to(dis, (650, 8), "balls:"+str(number_balls), pygame.Color("black"))

			pygame.display.update()
			clock.tick(60)
		
		pygame.quit()

Game()