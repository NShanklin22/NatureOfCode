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
fps = 1

black = (0, 0, 0)
blue = (0, 121, 150)
blue1 = (0,14,71)
white = (255, 255, 255)
red = (255,0,0)

scaler = 20
offset = 1
tick = 0
power = 0

pause = False
run = True

# Create the grid
Gridx = int(width/10)
Gridy = int(height/10)
GridArray = np.random.randint(0,2,(Gridx,Gridy))

print(GridArray)

while run:
    clock.tick(fps)
    screen.fill(black)

    GridArray = np.random.randint(0, 2, (Gridx, Gridy))

    for i in range(Gridx):
        for j in range(Gridy):
            if GridArray[i][j] == 1:
                pygame.draw.rect(screen, red, pygame.Rect(i*10 + 1, j* 10 + 1, 9, 9))
            else:
                pygame.draw.rect(screen, white, pygame.Rect(i*10 + 1, j* 10 + 1, 9, 9))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                pause = not pause

    pygame.display.update()

pygame.quit()
