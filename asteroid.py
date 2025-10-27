import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            sub_vector_1 = self.velocity.rotate(random_angle)
            sub_vector_2 = self.velocity.rotate(-random_angle)
            sub_radius = self.radius - ASTEROID_MIN_RADIUS

            sub_asteroid_1 = Asteroid(self.position.x, self.position.y, sub_radius)
            sub_asteroid_1.velocity = sub_vector_1 * 1.5
            sub_asteroid_2 = Asteroid(self.position.x, self.position.y, sub_radius)
            sub_asteroid_2.velocity = sub_vector_2 * 1.5

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
