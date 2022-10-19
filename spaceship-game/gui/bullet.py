import os
import pygame
from gui.sprites import MovingSprite

BULLET_IMAGE = (
    pygame.transform.scale(
        pygame.image.load(os.path.join('assets', 'bullet.webp')),
        (60, 40)
    )
)


class Bullet(MovingSprite):
    def __init__(self, *args):
        super().__init__(*args, velocity=10)

        self.image = BULLET_IMAGE
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self):
        super().update()

