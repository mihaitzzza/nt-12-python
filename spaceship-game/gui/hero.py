import os
import pygame
from gui.sprites import MovingSprite
from utility.constants import HEIGHT

HERO_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join('assets', 'man', 'hero.gif')),
    (200, 100)
)

HERO_MOVING_IMAGES = [
    pygame.transform.scale(
        pygame.image.load(os.path.join('assets', 'man', 'animation', f'frame_{i}_delay-0.05s.gif')),
        (200, 100)
    )
    for i in range(5)
]


class Hero(MovingSprite):
    def __init__(self, *args):
        super().__init__(*args, velocity=1, moving_images=HERO_MOVING_IMAGES)

        self.image = HERO_IMAGE
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = HEIGHT - self.rect.height - 1

    def update(self):
        if self._is_moving:
            super().update()
        else:
            self.image = HERO_IMAGE