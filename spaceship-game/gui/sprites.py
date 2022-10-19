import pygame
from utility.utils import MovingDirections
from utility.constants import WIDTH, HEIGHT


class MovingSprite(pygame.sprite.Sprite):
    def __init__(self, *args, velocity=1, moving_images=None):
        super().__init__(*args)

        self._velocity = velocity
        self._is_moving = False
        self._moving_images = moving_images or []
        self._move_image_index = 0

    def stop(self):
        self._is_moving = False

    def move(self, direction):
        self._is_moving = True

        if direction == MovingDirections.UP:
            if self.rect.y > 0:
                self.rect.y -= self._velocity
        elif direction == MovingDirections.RIGHT:
            if self.rect.x < (WIDTH - self.rect.width - 1):
                self.rect.x += self._velocity
        elif direction == MovingDirections.DOWN:
            if self.rect.y < (HEIGHT - self.rect.height - 1):
                self.rect.y += self._velocity
        elif direction == MovingDirections.LEFT:
            if self.rect.x > 0:
                self.rect.x -= self._velocity

    def update(self):
        if len(self._moving_images) > 0:
            self.image = self._moving_images[self._move_image_index]
            self._move_image_index += 1

            if self._move_image_index >= len(self._moving_images):
                self._move_image_index = 0
