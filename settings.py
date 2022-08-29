
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
        #Bullet setting
        self.bullet_speed = 0.4
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (60,60,60)