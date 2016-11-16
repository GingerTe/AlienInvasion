import sys
from time import sleep

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


def check_events(ai_settings, screen, stats, play_button, ship, alien_group, bullet_group):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullet_group)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship,
                              alien_group, bullet_group, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, play_button, ship, alien_group, bullet_group, mouse_x, mouse_y):
    """Start new game on press Play button"""
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        stats.reset_stats()
        stats.game_active = True

        # Delete aliens and bullets
        alien_group.empty()
        bullet_group.empty()

        # Create new fleet and place ship in the center of bottom side
        create_fleet(ai_settings, screen, ship, alien_group)
        ship.center_ship()


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


def check_alien_bottom(ai_settings, stats, screen, ship, alien_group, bullet_group):
    """Check if aliens reaches bottom side of the screen"""
    screen_rect = screen.get_rect()
    for alien in alien_group.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Same as ship collision
            ship_hit(ai_settings, stats, screen, ship, alien_group, bullet_group)


def update_alien_group(ai_settings, stats, screen, ship, alien_group, bullet_group):
    """Update all alien position in the fleet"""
    check_fleet_edge(ai_settings, alien_group)
    alien_group.update()

    # Checking collisions "alien-ship"
    if pygame.sprite.spritecollideany(ship, alien_group):
        ship_hit(ai_settings, stats, screen, ship, alien_group, bullet_group)

    check_alien_bottom(ai_settings, stats, screen, ship, alien_group, bullet_group)


def ship_hit(ai_settings, stats, screen, ship, alien_group, bullet_group):
    """Processing ships crash"""
    # Decreasing ship_left
    if stats.ship_left > 0:
        stats.ship_left -= 1

        alien_group.empty()
        bullet_group.empty()

        # Create new fleet and placing ship in the center
        create_fleet(ai_settings, screen, ship, alien_group)
        ship.center_ship()

        sleep(0.5)
    else:
        stats.game_active = False


def create_fleet(ai_settings, screen, ship, alien_group):
    """Create an alien fleet"""
    alien = Alien(ai_settings, screen)
    number_alien_x = get_alien_number(ai_settings, alien.rect.width)
    number_rows = get_alien_row(ai_settings, ship.rect.height, alien.rect.height)

    # Create first row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(ai_settings, screen, alien_group, alien_number, row_number)


def update_screen(ai_settings, screen, stats, ship, alien_group, bullet_group, play_button):
    """Update images on the screen and display new screen"""
    screen.fill(ai_settings.bg_color)
    # All bullets displaying beside images of ship and aliens
    for bullet in bullet_group:
        bullet.draw_bullet()
    ship.draw_ship()
    alien_group.draw(screen)
    if not stats.game_active:
        play_button.draw_button()

    # Show last shown screen
    pygame.display.flip()


def update_bullet_group(ai_settings, screen, ship, alien_group, bullet_group):
    """Updating bullet position and destroying old bullet"""
    # Updating bullet position
    bullet_group.update()

    # Removing bullets left for the edge of the screen
    for bullet in bullet_group.copy():
        if bullet.rect.bottom <= 0:
            bullet_group.remove(bullet)

    check_bullet_alien_collision(ai_settings, screen, ship, alien_group, bullet_group)


def check_bullet_alien_collision(ai_settings, screen, ship, alien_group, bullet_group):
    """Aliens and bullets collision processing"""
    # If bullet shot the alien delete both bullet and alien
    collisions = pygame.sprite.groupcollide(bullet_group, alien_group, True, True)
    if not alien_group:
        # Destroy existing bullets and create new fleet
        bullet_group.empty()
        create_fleet(ai_settings, screen, ship, alien_group)


def fire_bullet(ai_settings, screen, ship, bullet_group):
    """Fires bullet if maximum doesn't reached"""
    # New bullet creation and including it in to bullet_group
    if len(bullet_group) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullet_group.add(new_bullet)
