import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien

##Overall class to manage game assets and behavior
class AlienInvasion:

    ## initialize game
    def __init__(self):
        pygame.init()
        self.game_settings = Settings()
        self.screen = pygame.display.set_mode((self.game_settings.screen_width, self.game_settings.screen_height))
        self.ship = Ship(self)
        self.alien = Alien(self)
        pygame.display.set_caption("Alien Invasion")

    ## start main loop for a game and do all things
    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()


    def _check_events(self):
        ## listen for keyboart input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        ## Redraw the screen during each passing of the loop
        self.screen.fill(self.game_settings.bg_color)
        self.ship.blitme()
        self.alien.blitme()

        ## make the most recently refresh screen visible
        pygame.display.flip()

# make the game instance and run the game
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()