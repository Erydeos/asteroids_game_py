import pygame
from constants import *
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    _ = pygame.init()
    dt = 0.0
    time = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    # Game loop
    while True:
        log_state()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        _ = screen.fill("black")

        player.update(dt)
        player.draw(screen)

        pygame.display.flip()
        dt = time.tick(60) / 1000



if __name__ == "__main__":
    main()
