import pygame


class Button:
    def __init__(self, ai_settings, screen, msg):
        """Initialize button attrs"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set button size and params
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Create rect object of button and align button in the center
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen.center

        # Button message
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Convert msg to rectangle and align text"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
