import pygame
import numpy as np
import random

# the grid class will be utilized in other simulation applications
class Grid:
    def __init__(self, width, height, scale, offset):
        self.scale = int(scale)

        self.columns = int(height/scale)
        self.rows = int(width/scale)

        self.size = (self.rows, self.columns)
        self.grid_array = np.zeros(shape=(self.size),dtype=np.int8)
        self.offset = offset


    def simulate(self, off_color, on_color, surface, pause,player_color,powerColor):

        colorScale = 0

        for x in range(self.rows):
            for y in range(self.columns):
                y_pos = y * self.scale
                x_pos = x * self.scale
                if x < 19:
                    print(self.grid_array[x][y])
                    if self.grid_array[x][y] > 0:
                        self.grid_array[x+1][y] = self.grid_array[x][y] - 5

                colorScale = setColorScale(self.grid_array[x][y])

                if self.grid_array[x][y] == 0:
                    pygame.draw.rect(surface, off_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
                elif self.grid_array[x][y] > 0:
                    pygame.draw.rect(surface, (colorScale,0,0), [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
                else:
                    pygame.draw.rect(surface, off_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])

def setColorScale(gridArray):
    colorScale = 0
    if gridArray == 1:
        colorScale = 50
    elif gridArray == 2:
        colorScale = 100
    elif gridArray == 3:
        colorScale = 150
    elif gridArray == 4:
        colorScale = 200
    elif gridArray > 4:
        colorScale = 255
    else:
        colorScale == 0
    return colorScale
