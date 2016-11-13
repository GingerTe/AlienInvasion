import sys

import pygame

from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullet_group):
    """Reacts on keystrokes"""
    if event.key == pygame.K_RIGHT:
        # Move ship right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move ship left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullet_group)


def check_keyup_events(event, ship):
    """Reacts on releasing keys"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullet_group):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullet_group)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullet_group):
    """Update images on the screen and display new screen"""
    screen.fill(ai_settings.bg_color)
    # All bullets displaying beside images of ship and aliens
    for bullet in bullet_group:
        bullet.draw_bullet()
    ship.draw_ship()
    # Show last shown screen
    pygame.display.flip()


def update_bullet_group(bullet_group):
    """Updating bullet position and destroying old bullet"""
    # Updating bullet position
    bullet_group.update()

    # Removing bullets left for the edge of the screen
    for bullet in bullet_group.copy():
        if bullet.rect.bottom <= 0:
            bullet_group.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullet_group):
    """Fires bullet if maximum doesn't reached"""
    # New bullet creation and including it in to bullet_group
    if len(bullet_group) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullet_group.add(new_bullet)
