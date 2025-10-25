import pygame
from sys import exit
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from constants import *


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() ; dt = 0
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    cur_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    cur_board = AsteroidField()

    # Main loop
    game_on = True
    while game_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for actor in updatable:
            actor.update(dt)
        for asteroid in asteroids:
            if cur_player.collides_with(asteroid):
                print("Game over!")
                exit(0)
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
