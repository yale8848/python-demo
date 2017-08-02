
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, screen, ship):
        super().__init__()

        self.speed_factor = 0.5
        self.width = 3
        self.height = 15
        self.color = 60,60,60

        self.screen = screen
        self.rect = pygame.Rect(0, 0, self.width,self.height)

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)
        self.ship = ship
        self.is_dispper = False;

    def lanuch(self):
        self.rect.top = self.ship.rect.top
        self.rect.centerx = self.ship.rect.centerx
        self.y = self.ship.rect.y

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        if self.rect.bottom < 0:
            self.is_dispper = True
            return
        pygame.draw.rect(self.screen, self.color, self.rect)
