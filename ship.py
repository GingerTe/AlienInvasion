import pygame


class Ship:
    """"Class for ship object"""

    def __init__(self, ai_settings, screen):
        """Initialize sheep and set start position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Download ship image and get it rectangle
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Every new ship appears in bottom part of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Saving real coordinates of ship center
        self.center = float(self.rect.centerx)
        # Moving flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updates the ship's position considering flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect attribute based in self.center
        self.rect.centerx = self.center

    def blitme(self):
        """"Draws sheep in the current position"""
        self.screen.blit(self.image, self.rect)
