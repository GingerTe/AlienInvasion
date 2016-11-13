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

    # Start main cycle of the game
    while True:
        # Caption keyboard and mouse events
        game_functions.check_events(ship)
        ship.update_position()
        # Screen redraws each time through the loop
        game_functions.update_screen(ai_settings, screen, ship)


run_game()
