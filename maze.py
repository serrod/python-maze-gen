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
RESOLUTION = 20

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

class maze:
    def __init__(self, size):
        self.size = size
        self.grid = []
    
    def setup(self):
        for i in range(self.size):
            for j in range(self.size):
                self.grid.append(node(i,j))

    def get_grid(self):
        return self.grid

def draw(maze):
    WINDOW.fill(BLACK)

    for i in range(RESOLUTION):
        for j in range(RESOLUTION):
            pygame.draw.rect(WINDOW,GRAY,[j*(WIDTH/RESOLUTION),i*(HEIGHT/RESOLUTION),(WIDTH/RESOLUTION)-1,(HEIGHT/RESOLUTION)-1])

def main():
    run = True
    clock = pygame.time.Clock()

    m = maze(RESOLUTION)
    m.setup()
    print(len(m.grid))

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw(m.get_grid)
        pygame.display.update()

    pygame.quit

if __name__ == "__main__":
    main()