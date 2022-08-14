import sys
import pygame

##Overall class to manage game assets and behavior
class AlienInvasion:

    ## initialize game
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        ## set background color
        self.bg_color = (240,240,240)

    ## start main loop for a game
    def run_game(self):
        while True:
        ## listen for keyboart input
            for event in pygame.event.get():
                print(event)
                if event == pygame.QUIT:
                    sys.exit()
            ## Redraw the screen during each passing of the loop
            self.screen.fill(self.bg_color)
            ## make the most recently refresh screen visible
            pygame.display.flip()

# make the game instance and run the game
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
