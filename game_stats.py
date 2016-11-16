import os
class GameStats:
    """Statistic tracking"""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings

        self.high_score = 0
        if os.path.isfile("high_score.txt"):
            with open("high_score.txt") as f:
                score = f.read().strip()
                if score:
                    self.high_score = int(score)

        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics, changind during the game"""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
