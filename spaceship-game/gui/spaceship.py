import os
import pygame
from gui.sprites import MovingSprite

SPACESHIP_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join('assets', 'rocket', 'spaceship.png')),
    (100, 120)
)

SPACESHIP_MOVE_IMAGES = [
    pygame.transform.scale(
        pygame.image.load(os.path.join('assets', 'rocket', 'animation', f'frame_{i if i > 99 else f"0{i}"}_delay-0.04s.png')),
        (100, 120)
    )
    for i in range(25, 122)
]

VELOCITY = 1


class Spaceship(MovingSprite):
    def __init__(self, *args):
        super().__init__(*args, velocity=VELOCITY, moving_images=SPACESHIP_MOVE_IMAGES)

        self.image = SPACESHIP_IMAGE
        self.rect = self.image.get_rect()
        self.rect.center = (300, 300)

    def update(self):
        if self._is_moving:
            super().update()
        else:
            self.image = SPACESHIP_IMAGE
