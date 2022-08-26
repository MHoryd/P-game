import pygame

## class to manage ship
class Ship:
    ## initialize ship and set it's starting position
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        ##load ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        ## start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        #mmovement flag
        self.moving_right = False
        self.moving_left = False
        self.setting = ai_game.game_settings
        # store decimal value fo ships horizontal position
        self.x = float(self.rect.x)



    def blitme(self):
        ##draw ship at current loation
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right: 
            self.x += self.setting.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.setting.ship_speed

        # update rect object from self x
        self.rect.x = self.x