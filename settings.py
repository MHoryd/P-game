
## class to store all settings
import pygame.time


class Settings:
    def __init__(self):
        ##initialize game settings

        #screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (50,50,230)
        self.ship_speed = 0.5