import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):

	def __init__(self, x: float, y: float, radius: float):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

	def update(self, dt):
		self.position += self.velocity * dt

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			log_event("asteroid_split")
			angle = random.uniform(20, 50)
			pos_angle = self.velocity.rotate(angle)
			neg_angle = self.velocity.rotate(0 - angle)
			new_radius = self.radius - ASTEROID_MIN_RADIUS
			first_new_roid = Asteroid(self.position.x, self.position.y, new_radius)
			first_new_roid.velocity = pos_angle * 1.2
			second_new_roid = Asteroid(self.position.x, self.position.y, new_radius)
			second_new_roid.velocity = neg_angle * 1.2
