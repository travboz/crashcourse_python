import sys

import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavioiur."""
    def __init__(self):
        """Initiliase the game, create game resources."""
        pygame.init()

        # defining a clock to control the framerate of the game
        self.clock = pygame.tick.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """State the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


            # Make the most recently drawn screen visible
            pygame.display.flip()
            # setting the clock to a tick/framerate of 60fps
            self.clock.tick(60) # 60 fps

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()