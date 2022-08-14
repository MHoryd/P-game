import sys
import pygame
from settings import Settings

##Overall class to manage game assets and behavior
class AlienInvasion:

    ## initialize game
    def __init__(self):
        pygame.init()
        self.game_settings = Settings()
        self.screen = pygame.display.set_mode((self.game_settings.screen_width, self.game_settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        ## set background color

    ## start main loop for a game
    def run_game(self):
        while True:
        ## listen for keyboart input
            for event in pygame.event.get():
                print(event)
                if event == pygame.QUIT:
                    sys.exit()
            ## Redraw the screen during each passing of the loop
            self.screen.fill(self.game_settings.bg_color)
            ## make the most recently refresh screen visible
            pygame.display.flip()

# make the game instance and run the game
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
