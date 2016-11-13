class GameStats():
    """Statistic tracking"""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """Initialize statistics, changind during the game"""
        self.ship_left = self.ai_settings.ship_limit
