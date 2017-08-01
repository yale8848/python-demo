import sys
import pygame

from game.alien.Setting import *
from game.alien.Ship import  Ship

def check_event(ship):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.move_right()
                elif event.key == pygame.K_LEFT:
                    ship.move_left()
            elif event.type == pygame.KEYUP:
                ship.stop_moving()

def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()

def run_game():
    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(screen)
    pygame.display.set_caption("Alien Invasion")

    while True:
        check_event(ship)
        ship.update()
        update_screen(ai_settings,screen,ship)
run_game()