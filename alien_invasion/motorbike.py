import pygame

class Motorbike:
    """A class to manage the motorbike."""
    def __init__(self, blue_sky):
        """Init bike and its starting place on grid."""
        self.screen = blue_sky.screen
        self.screen_rect = blue_sky.screen.get_rect()

        # loading bike img
        self.image = pygame.image.load('/Users/travb/Desktop/learning_python/learning_python_git/crashcourse_python/alien_invasion/blue_sky_img/spr_bike1_0.png')
        self.rect = self.image.get_rect()

        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
