import pygame


class Alien(pygame.sprite.Sprite):
    """Class representing one alien"""

    def __init__(self, ai_settings, screen):
        """Initializing an alien and setting it init position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Downloading an alien image and setting up rect attribute
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Every new alien appears on the left top edge of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Saving an exact position of an alien
        self.c = float(self.rect.x)

    def draw_alien(self):
        """Displaying an alien in current position"""
        self.screen.blit(self.image, self.rect)

    def check_edge(self):
        """Returns True if alien reaches screen edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x
