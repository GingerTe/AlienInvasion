import sys

import pygame

from alien import Alien
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
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


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


def get_alien_number(ai_settings, alien_width):
    """Count alien number in row"""
    alien_width_with_space = 2 * alien_width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / alien_width_with_space)
    return number_alien_x


def get_alien_row(ai_settings, ship_height, alien_height):
    """Get row number that fit on the screen"""
    alien_height_with_space = 2 * alien_height
    available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
    number_rows = int(available_space_y / alien_height_with_space)
    return number_rows


def create_alien(ai_settings, screen, alien_group, alien_number, row_number):
    """Create an alien and placed in into the row"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number  # + (1- (-1) ** row_number) * alien_width
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien_group.add(alien)


def check_fleet_edge(ai_settings, alien_group):
    """Reacts on alien reaching screen edge"""
    for alien in alien_group.sprites():
        if alien.check_edge():
            change_fleet_direction(ai_settings, alien_group)
            break


def change_fleet_direction(ai_settings, alien_group):
    """Lowers the entire fleet and changes the direction of the fleet"""
    for alien in alien_group.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_alien_group(ai_settings, alien_group):
    """Update all alien position in the fleet"""
    check_fleet_edge(ai_settings, alien_group)
    alien_group.update()


def create_fleet(ai_settings, screen, ship, alien_group):
    """Create an alien fleet"""
    alien = Alien(ai_settings, screen)
    number_alien_x = get_alien_number(ai_settings, alien.rect.width)
    number_rows = get_alien_row(ai_settings, ship.rect.height, alien.rect.height)

    # Create first row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(ai_settings, screen, alien_group, alien_number, row_number)


def update_screen(ai_settings, screen, ship, alien_group, bullet_group):
    """Update images on the screen and display new screen"""
    screen.fill(ai_settings.bg_color)
    # All bullets displaying beside images of ship and aliens
    for bullet in bullet_group:
        bullet.draw_bullet()
    ship.draw_ship()
    alien_group.draw(screen)
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
