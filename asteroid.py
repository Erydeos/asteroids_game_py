import random
from termios import VEOL2

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
import pygame
from typing import override

from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    @override
    def draw(self, screen):
        _= pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    @override
    def update(self, dt: float) -> None:
        self.position += self.velocity

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            vel1 = self.velocity.rotate(angle)
            vel2 = self.velocity.rotate(-angle)
            rad = self.radius - ASTEROID_MIN_RADIUS
            rock1 = Asteroid(self.position.x, self.position.y, rad)
            rock1.velocity = vel1 * 1.2
            rock2 = Asteroid(self.position.x, self.position.y, rad)
            rock2.velocity = vel2 * 1.2
