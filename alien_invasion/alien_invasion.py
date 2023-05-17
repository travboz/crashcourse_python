import sys
import pygame

from alien_invasion_settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavioiur."""
    def __init__(self):
        """Initiliase the game, create game resources."""
        pygame.init()

        # defining a clock to control the framerate of the game
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        # setting the background colour
        # self.bg_color = (230, 230, 230)

        self.ship = Ship(self)

    def run_game(self):
        """State the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            # setting the clock to a tick/framerate of 60fps
            self.clock.tick(60) # 60 fps

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()