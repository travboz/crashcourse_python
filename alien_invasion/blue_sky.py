import pygame
import sys

class BlueSky:
    """Make a pygame window with a blue background."""
    def __init__(self):
        pygame.init() # init the game
        self.clock = pygame.time.Clock()
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (55, 55, 230)
        self.screen = pygame.display.set_mode((1200, 800))

        pygame.display.set_caption("Blue Background")

    def run_game(self):
        """State the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            # setting the clock to a tick/framerate of 60fps
            self.clock.tick(60) # 60 fps

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw screen during each pass through the loop
        self.screen.fill(self.bg_color)

        # Make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    game = BlueSky()
    game.run_game()