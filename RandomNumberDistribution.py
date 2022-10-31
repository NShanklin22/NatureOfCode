import pygame
import time
import random
import numpy as np
import os
import grid
from perlin_noise import PerlinNoise

os.environ["SDL_VIDEO_CENTERED"]='1'

#Screen Resolution
width, height = 400,400
size = (width, height)

# Pygame initialization
pygame.init()
pygame.display.set_caption("GRID TIME")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 15

# Set the color of the screen to white
screen.fill((255,255,255))

# Declare a list of size 20 containing nothing
RandomCounts = [0] * 20
RandomNumber = 0

print(RandomCounts)
font = pygame.font.Font('freesansbold.ttf', 12)

run = True

while run:
    clock.tick(fps)

    RandomNumber = random.random()

    for i in range(len(RandomCounts)):
        RandomNumber = random.randint(0, 10)
        RandomCounts[i] += RandomNumber
        text = font.render('{}'.format(i), True, (0,0,0), (255,255,255))
        textRect = text.get_rect()
        screen.blit(text, (5+i*21,300))
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(4 +i*21 + 1, 300 -RandomCounts[i], 10, RandomCounts[i]))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                pause = not pause

    pygame.display.update()

#     int
# index = int(random(randomCounts.length));
# randomCounts[index] + +;
#
# stroke(0);
# fill(175);
# int
# w = width / randomCounts.length;
# Graphing
# the
# results
# for (int x = 0; x < randomCounts.length; x++) {
#     rect(x * w, height - randomCounts[x], w - 1, randomCounts[x]);
# }
# }