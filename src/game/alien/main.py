import sys
import pygame

from game.alien.Setting import *
from game.alien.Ship import  Ship
from  game.alien.Bullet import  Bullet
from pygame.sprite import Group
from game.alien.UFO import UFO
from  pygame.sprite import Sprite

key_stack = []
ufo_num = 1
ufo_dead_num = 0

def check_event(ship,screen,bullets):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    key_stack.append(pygame.K_RIGHT)
                    ship.move_right()
                elif event.key == pygame.K_LEFT:
                    key_stack.append(pygame.K_LEFT)
                    ship.move_left()
                elif event.key == pygame.K_SPACE:
                    key_stack.append(pygame.K_SPACE)
                    bullet = Bullet(screen, ship)
                    bullets.add(bullet)
            elif event.type == pygame.KEYUP:
                if key_stack.__len__() !=0 and key_stack.pop() != pygame.K_SPACE:
                    ship.stop_moving()

def update_screen(ai_settings, screen, ship,bullets,ufos):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    for bullet in bullets:
        bullet.draw_bullet()
    for ufo in ufos:
        ufo.blitme()
    pygame.display.flip()

def update_bullets(bullets):

    for bullet in bullets.copy():
        if bullet.is_dispper == True:
            bullets.remove(bullet)
            continue
        bullet.update()

def update_ufo(ufos,bullets,ship):
    global  ufo_dead_num,ufo_num

    for ufo in ufos.copy():
        if ufo.is_dispper == True:
            ufos.remove(ufo)
            continue
        s = pygame.sprite.spritecollideany(ufo,bullets)
        if s != None:
            ufos.remove(ufo)
            ufo_dead_num += 1
            if ufo_dead_num == 3:
                ufo_dead_num=0
                ufo_num += 1
                ship.ship_speed_factor +=0.1

            bullets.remove(s)
            continue
        ufo.update()

def create_ufo(ufos,screen,setting):
    if len(ufos) < ufo_num:
        ufo = UFO(screen, setting)
        if pygame.sprite.spritecollideany(ufo,ufos) == None:
            ufos .add(ufo)
        else:
            print("hint")


def run_game():
    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(screen)
    pygame.display.set_caption("Alien Invasion")
    bullets = Group()

    ufos = Group()

    while True:
        check_event(ship,screen,bullets)
        ship.update()
        update_bullets(bullets)
        create_ufo(ufos,screen,ai_settings)
        update_ufo(ufos,bullets,ship)
        update_screen(ai_settings,screen,ship,bullets,ufos)


run_game()