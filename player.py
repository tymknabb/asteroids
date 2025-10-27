import pygame
from circleshape import CircleShape
from shot import Shot
from constants import *


class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0
        self.acceleration = pygame.Vector2(0, 0)
        self.accel_factor = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def thrust(self, accel_factor, dt):
        self.acceleration = pygame.Vector2(0, 1).rotate(self.rotation) * accel_factor
        self.velocity += self.acceleration * dt

    def move(self, dt):
        self.position += self.velocity * dt

    def shoot(self):
        if self.shot_timer == 0:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shot_timer = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.thrust(PLAYER_ACCELERATION, dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_s]:
            self.thrust(-PLAYER_ACCELERATION, dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.move(dt)
        if self.velocity.length() > PLAYER_MAX_SPEED:
            self.velocity.normalize_ip()
            self.velocity *= PLAYER_MAX_SPEED

        self.shot_timer = max(0, self.shot_timer - dt)
