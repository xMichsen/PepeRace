import math
import random
import sys
import pygame
from pygame.locals import *

def collision(x1,y1,x2,y2):
    distance = math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))
    if distance < 60:
        return True
    else:
        return False

pygame.init()
pygame.display.set_caption("Pepe race")
fps = 60
fpsClock = pygame.time.Clock()

width, height = 1400, 900
screen = pygame.display.set_mode((width, height))

money = 3000
font = pygame.font.SysFont('Comic Sans MS', 30)

pepe1 = pygame.image.load("pepe1.png")
pepe2 = pygame.image.load("pepe2.png")
pepe3 = pygame.image.load("pepe3.png")
pepe4 = pygame.image.load("pepe4.png")
pepe5 = pygame.image.load("pepe5.png")
bg = pygame.image.load("bg.png")
bg = pygame.transform.scale(bg,(width,height))

pepes = [pepe1,pepe2,pepe3,pepe4,pepe5]
pepes_x = [width/20,width/20,width/20,width/20,width/20]
pepes_y = [height/10 ,height/10 + 150,height/10 + 320,height/10 + 500,height/10 + 650]
pepes_x_dif = [0,0,0,0,0]
pepes_cost = 500
hit = 0
start = False
chosen_pepe = None
last_winner = -8
game_over = False

while True:
    screen.fill((255, 255, 255))
    screen.blit(bg,(0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if not start:
        pepes_x = [width / 20, width / 20, width / 20, width / 20, width / 20]
        for i in range(len(pepes)):
            text_lastwinner = font.render("Wygral zawodnik nr " + str(last_winner + 1) , True, (0, 0, 0), (255, 131, 0))
            mousepos = pygame.mouse.get_pos()
            screen.blit(pepes[i],(pepes_x[i],pepes_y[i]))
            screen.blit(text_lastwinner, (400, 50))
            if collision(pepes_x[i]+50,pepes_y[i],mousepos[0],mousepos[1]) and pygame.mouse.get_pressed()[0]:
                money -= pepes_cost
                chosen_pepe = i
                print(chosen_pepe)
                start = True
    if start:
        for i in range(len(pepes)):
            text_chosen = font.render("Wybrales " + str(chosen_pepe + 1) + " zawodnika", True, (0, 0, 0), (255, 131, 0))
            pepes_x_dif[i] = random.uniform(0.1,10)
            pepes_x[i] += pepes_x_dif[i]
            screen.blit(pepes[i], (pepes_x[i], pepes_y[i]))
            screen.blit(text_chosen, (400, 50))
            if pepes_x[i] > 1300:
                if i == chosen_pepe:
                    money += 1000
                last_winner = i
                start = False



    text_money = font.render('Kaska: ' + str(money) + "$", True, (0, 0, 0), (255,131,0))

    screen.blit(text_money,(100,50))

    pygame.display.flip()
    fpsClock.tick(fps)
