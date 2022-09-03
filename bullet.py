import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #Class to manage bullets fired from ship

    def __init__(self, ai_game):
        #Create bullet object in ship's current position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.game_settings
        self.colour = self.settings.bullet_colour
        
        #Create bullet rect at (0,0) and set correct position.
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        #move bullet up the screen
        # update the rect position
        self.y -= self.settings.bullet_speed
        #update rect position
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.colour, self.rect)
