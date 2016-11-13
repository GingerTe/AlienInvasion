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
