import pygame

import game_functions
from settings import Settings
from ship import Ship


def run_game():
    """Game initializing and window object creation"""
    ai_settings = Settings()

    pygame.init()
    # Set screen size and caption
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.screen_caption)

    # Create a ship
    ship = Ship(ai_settings, screen)

    # Creating group for bullets storing
    bullet_group = pygame.sprite.Group()

    # Start main cycle of the game
    while True:
        # Caption keyboard and mouse events
        game_functions.check_events(ai_settings, screen, ship, bullet_group)
        ship.update()
        game_functions.update_bullet_group(bullet_group)

        # Screen redraws each time through the loop
        game_functions.update_screen(ai_settings, screen, ship, bullet_group)


run_game()
