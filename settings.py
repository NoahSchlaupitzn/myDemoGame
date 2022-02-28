
class Settings:
    """a class to store all settings for alien invasion"""

    def __init__(self):
        """initialize the games settings"""
        # screen setting
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (50, 50, 50)
        self.bullets_allowed = 4

        # ship settings
        self.ship_speed = 1.5

        # bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3.0
        self.bullet_height = 10.0
        self.bullet_color = (0, 180, 0)

        # alien settings
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

