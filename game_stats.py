class GameStats:
    """Statistic tracking"""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings

        # Saving hign score during session
        self.high_score = 0

        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics, changind during the game"""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
