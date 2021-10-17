import random
import time
import pygame
from pygame.constants import RESIZABLE

WIDTH = 500
HEIGHT = 500
WINDOW_SIZE = (WIDTH,HEIGHT)

WINDOW = pygame.display.set_mode(WINDOW_SIZE,)
pygame.display.set_caption("python maze generation")

WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (128,128,128)
RESOLUTION = 10

FPS = 60

class node:
    def __init__(self,x,y):
        self.east = True
        self.west = True
        self.north = True
        self.south = True

        self.visited = False

        self.x = x
        self.y = y

    def convert_coords(self):
        return self.x+(self.y*RESOLUTION)

def convert_coords(x,y):
    return x+(y*RESOLUTION)

def draw(grid):
    WINDOW.fill(WHITE)

    for i in range(RESOLUTION):
        for j in range(RESOLUTION):

            if grid[convert_coords(j,i)].visited == False:
                pygame.draw.rect(WINDOW,GRAY,[j*(WIDTH/RESOLUTION),i*(HEIGHT/RESOLUTION),(WIDTH/RESOLUTION)-2,(HEIGHT/RESOLUTION)-2])
            else:
                pygame.draw.rect(WINDOW,BLACK,[j*(WIDTH/RESOLUTION),i*(HEIGHT/RESOLUTION),(WIDTH/RESOLUTION)-2,(HEIGHT/RESOLUTION)-2])

def main():
    run = True
    clock = pygame.time.Clock()
    
    grid = []
    stack = []
    num_vis = 0

    for i in range(RESOLUTION):
            for j in range(RESOLUTION):
                grid.append(node(j,i))

    grid[5].visited = True
    grid[26].visited = True

    print(grid[14].visited)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw(grid)
        pygame.display.update()

    pygame.quit

if __name__ == "__main__":
    main()