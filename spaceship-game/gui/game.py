import pygame
from utility.constants import WIDTH, HEIGHT
from gui.spaceship import Spaceship
from gui.hero import Hero
from gui.bullet import Bullet
from utility.utils import MovingDirections


class Game:
    def __init__(self):
        self._is_running = True
        self._clock = pygame.time.Clock()
        self._screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self._sprites = pygame.sprite.Group()
        self._spaceship = Spaceship()
        self._sprites.add(self._spaceship)
        self._hero = Hero()
        self._sprites.add(self._hero)
        self._bullet = None
        pygame.display.set_caption('Spaceship Explosion')

    def _check_events(self):
        # Inside for loop we have only one event.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._is_running = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                left_click, _, _ = pygame.mouse.get_pressed()
                if left_click:
                    self._bullet = Bullet()
                    self._sprites.add(self._bullet)

        # Outside for loop we get events for each frame.
        key_pressed = pygame.key.get_pressed()

        # Move spaceship
        move_to_directions = {
            MovingDirections.UP: key_pressed[pygame.K_w],
            MovingDirections.LEFT: key_pressed[pygame.K_a],
            MovingDirections.DOWN: key_pressed[pygame.K_s],
            MovingDirections.RIGHT: key_pressed[pygame.K_d]
        }

        if True in move_to_directions.values():
            for direction, value in move_to_directions.items():
                if value is True:
                    self._spaceship.move(direction)
        else:
            self._spaceship.stop()

        # Move hero
        if key_pressed[pygame.K_RIGHT]:
            self._hero.move(MovingDirections.RIGHT)
        else:
            self._hero.stop()

        if self._bullet is not None:
            self._bullet.move(MovingDirections.RIGHT)

    def _draw(self):
        self._screen.fill((150, 150, 150))  # (R, G, B) / (R, G, B, A)
        self._sprites.draw(self._screen)
        self._sprites.update()

        pygame.display.update()

    def run(self):
        while self._is_running:
            self._check_events()
            self._draw()
            self._clock.tick(60)  # Set FPS (Frame Per Second)

        pygame.quit()
