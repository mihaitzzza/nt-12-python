import pygame


class Game:
    def __init__(self):
        self._is_running = True
        self._clock = pygame.time.Clock()
        self._screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Spaceship Explosion')

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._is_running = False
                break

    def _draw(self):
        self._screen.fill((255, 255, 255))  # (R, G, B) / (R, G, B, A)
        pygame.display.update()

    def run(self):
        while self._is_running:
            self._check_events()
            self._draw()
            self._clock.tick(60)  # Set FPS (Frame Per Second)

        pygame.quit()
