import pygame
import time
import random
import numpy as np
import os
import grid

os.environ["SDL_VIDEO_CENTERED"]='1'

#resolution
width, height = 400,400
size = (width, height)

pygame.init()
pygame.display.set_caption("GRID TIME")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 30

black = (0, 0, 0)
blue = (0, 121, 150)
blue1 = (0,14,71)
white = (255, 255, 255)
red = (255,0,0)

powerColor = {"1":(50,0,0),"2":(100,0,0),"3":(150,0,0),"4":(200,0,0),"5":(250,0,0)}
power = 0

scaler = 20
offset = 1
tick = 0
power = 0

Grid = grid.Grid(width,height, scaler, offset)
#Grid.random2d_array()

pause = False
run = True
while run:
    clock.tick(fps)
    screen.fill(black)

    if tick == 5:
        tick = 0
        print(Grid.grid_array)
    else:
        tick += 1


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                pause = not pause
    Grid.simulate(off_color=white, on_color=blue1, surface=screen, pause=pause,player_color=red,powerColor=powerColor)

    # if pygame.mouse.get_pressed()[0]:
    #     mouseX, mouseY = pygame.mouse.get_pos()
    #     Grid.HandleMouse(mouseX, mouseY)

    pygame.display.update()

pygame.quit()
