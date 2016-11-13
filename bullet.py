import pygame


class Bullet(pygame.sprite.Sprite):
    """Class for controlling bullets ship issued"""

    def __init__(self, ai_settings, screen, ship):
        """Create bullet object in current ship position"""
        super().__init__()
        self.screen = screen

        # Create bullet in position (0, 0) and set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Bullet -position stores in real format
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Moves the bullet up the screen"""
        # Updating bullet position in real format
        self.y -= self.speed_factor
        # Updating rectangle position
        self.rect.y = self.y

    def draw_bullet(self):
        """Displaying the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
