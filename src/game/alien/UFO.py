import pygame
from  pygame.sprite import Sprite
import random


class UFO(Sprite):
    def __init__(self,screen,setting):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('img/ufo.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,setting.screen_width-self.rect.width)
        self.rect.y = 100
        self.y = random.randint(-200,0)
        self.speed = 0.2
        self.is_dispper = False

    def update(self):
        self.y += self.speed
        self.rect.y = self.y
        if self.rect.y>=self.screen.get_rect().bottom:
            self.is_dispper = True


    def blitme(self):
        self.screen.blit(self.image,self.rect)
