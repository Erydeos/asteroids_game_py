from ast import AsyncFunctionDef
import sys

import pygame
from asteroid import Asteroid
from constants import *
from logger import log_event, log_state
from player import Player
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    _ = pygame.init()
    dt = 0.0
    time = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (updatable, drawable, shots)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    # Game loop
    while True:
        log_state()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        _ = screen.fill("black")


        updatable.update(dt)

        for rock in asteroids:
            if rock.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(rock):
                    log_event("asteroid_shot")
                    shot.kill()
                    rock.kill()

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()
        dt = time.tick(60)/1000



if __name__ == "__main__":
    main()
