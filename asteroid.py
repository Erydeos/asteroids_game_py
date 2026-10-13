from circleshape import CircleShape
from constants import LINE_WIDTH
import pygame
from typing import override

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    @override
    def draw(self, screen):
        _= pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    @override
    def update(self, dt: float) -> None:
        self.position += self.velocity
