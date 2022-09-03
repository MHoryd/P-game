import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
from bullet import Bullet

##Overall class to manage game assets and behavior
class AlienInvasion:

    ## initialize game
    def __init__(self):
        pygame.init()
        self.game_settings = Settings()
        self.screen = pygame.display.set_mode((self.game_settings.screen_width, self.game_settings.screen_height))
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.alien = Alien(self)
        pygame.display.set_caption("Alien Invasion")

    ## start main loop for a game and do all things
    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()

    def _check_events(self):
        ## listen for keyboart input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self, event):
        # respond to key press
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_event(self,event):
        # respond to key press
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        ## Redraw the screen during each passing of the loop
        self.screen.fill(self.game_settings.bg_color)
        self.ship.blitme()
        self.alien.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        ## make the most recently refresh screen visible
        pygame.display.flip()


    def _fire_bullet(self):
        if len(self.bullets) < self.game_settings.bullets_allowed:
            #Create bullet and add bullet to bullet group
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        #update position of bullets and get rid of old bullets.
        # update bullet position
        self.bullets.update()
        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


# make the game instance and run the game
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()