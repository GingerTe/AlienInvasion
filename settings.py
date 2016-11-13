class Settings:
    """Store all the game settings"""

    def __init__(self):
        "Initialize game settings"
        # Screen params
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.screen_caption = "Alien Invasion"

        # Ship settings
        self.ship_speed_factor = 1.5

        # Bullet params
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        # At any moment on the screen can be a maximum of three bullets
        self.bullet_allowed = 3
