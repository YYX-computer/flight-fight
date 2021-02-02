from tkinter.messagebox import showinfo
from pygame.locals import *
import tkinter as tk
from random import *
import pygame
base = tk.Tk()
base.geometry('0x0')
base.resizable(False,False)
def intersect_p2f(p,f):
    return pygame.Rect(f).collidepoint(*p)
def intersect_f2f(f1,f2):
    return pygame.Rect(f1).colliderect(pygame.Rect(f2))
def main():
    WIDTH,HEIGHT = 480,640
    scr = pygame.display.set_mode((WIDTH,HEIGHT))
    bg = pygame.image.load('background.jpg')
    fighter = pygame.image.load('fighter.jpg')
    plane_enemy = pygame.image.load('plane_enemy.jpg')
    enemy_bullet = pygame.image.load('enemy_bullet.jpg')
    fighter_bullet = pygame.image.load('fighter_bullet.jpg')
    planes = []
    enemy_bullets = []
    fighter_x = 0
    fighter_bullets = []
    score = 0
    n = 1
    R_P = L_P = False
    while(1):
        for i in enemy_bullets:
            if(intersect_p2f(i,((fighter_x, HEIGHT - 64),(fighter_x, HEIGHT - 64)))):
                return score
        for i in range(len(planes)):
            if(i >= len(planes)):
                break
            for j in fighter_bullets:
                if(intersect_p2f(j,(planes[i],(planes[i][0] + 64,planes[i][1] + 64)))):
                    planes.pop(i)
                    score += 10
        pygame.display.update()
        scr.blit(bg,(0,0))
        n = (n + 1) % 600
        if(not n):
            x = randint(0,WIDTH - 64)
            y = randint(0,HEIGHT / 2)
            planes.append((x,y))
        elif(not n % 90):
            for i in range(len(planes)):
                enemy_bullets.append((planes[i][0] + 32, planes[i][1] + 64))
            fighter_bullets.append((fighter_x + 32, HEIGHT - 64))
        elif(not n % 8):
            if(L_P and (not R_P)):
                fighter_x = max(fighter_x - 5, 0)
            if(R_P and (not L_P)):
                fighter_x = min(fighter_x + 5, WIDTH - 64)
        for i in range(len(planes)):
            planes[i] = (planes[i][0],planes[i][1] + 0.5)
            scr.blit(plane_enemy,planes[i])
        scr.blit(fighter, (fighter_x, HEIGHT - 64))
        for i in range(len(enemy_bullets)):
            if (i >= len(enemy_bullets)):
                break
            enemy_bullets[i] = (enemy_bullets[i][0],enemy_bullets[i][1] + 5)
            if(enemy_bullets[i][1] >= WIDTH):
                enemy_bullets.pop(i)
            if (i >= len(enemy_bullets)):
                break
            scr.blit(enemy_bullet,enemy_bullets[i])
        for i in range(len(fighter_bullets)):
            if (i >= len(fighter_bullets)):
                break
            fighter_bullets[i] = (fighter_bullets[i][0],fighter_bullets[i][1] - 5)
            if(fighter_bullets[i][1] <= 0):
                fighter_bullets.pop(i)
            if (i >= len(fighter_bullets)):
                break
            scr.blit(fighter_bullet,fighter_bullets[i])
        for ev in pygame.event.get():
            if(ev.type == QUIT):
                exit()
            elif(ev.type == KEYDOWN):
                if(ev.key == K_LEFT):
                    L_P = True
                elif(ev.key == K_RIGHT):
                    R_P = True
            elif(ev.type == KEYUP):
                if (ev.key == K_LEFT):
                    L_P = False
                elif (ev.key == K_RIGHT):
                    R_P = False
if(__name__ == '__main__'):
    while(1):
        score = main()
        showinfo('GAMEOVER!','GAMEOVER!score:%s'%score)
