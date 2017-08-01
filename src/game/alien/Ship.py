import pygame

class Ship():

    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('img/fly.png')
        self.rect  = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = (self.screen_rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.init_moving()
        self.ship_speed_factor = 0.2
        self.center = float(self.screen_rect.centerx)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def init_moving(self):
        self.moving_right = False
        self.moving_left = False

    def move_right(self):
        self.init_moving()
        self.moving_right = True

    def move_left(self):
        self.init_moving()
        self.moving_left = True

    def stop_moving(self):
        self.init_moving()

    def update(self):
        if self.moving_left == True:
            self.center -= float(self.ship_speed_factor)
        if self.moving_right == True:
            self.center += float(self.ship_speed_factor)
        self.rect.centerx = self.center

