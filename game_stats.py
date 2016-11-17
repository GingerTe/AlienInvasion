import json
import os


class GameStats:
    """Statistic tracking"""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.score_path = "high_score.txt"
        self.high_score = 0
        self.champion_name = ""
        if os.path.isfile(self.score_path):
            with open(self.score_path) as f:
                champion = json.load(f)[0]
                self.high_score = int(champion[0])
                self.champion_name = champion[1]

        self.reset_stats()
        self.game_active = False
        self.ask_name = False

    def reset_stats(self):
        """Initialize statistics, changing during the game"""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
