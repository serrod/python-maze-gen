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
RED = (255,0,0)
RESOLUTION = 50

FPS = 60

class node:
    def __init__(self):
        self.east = True
        self.south = True

        self.visited = False

def convert_coords(x,y):
    return x+(y*RESOLUTION)

def draw(grid,stack):
    WINDOW.fill(WHITE)

    for i in range(RESOLUTION):
        for j in range(RESOLUTION):

            if grid[convert_coords(j,i)].visited == False:
                pygame.draw.rect(WINDOW,WHITE,[j*(WIDTH/RESOLUTION),i*(HEIGHT/RESOLUTION),(WIDTH/RESOLUTION)-2,(HEIGHT/RESOLUTION)-2])
            else:
                pygame.draw.rect(WINDOW,BLACK,[j*(WIDTH/RESOLUTION),i*(HEIGHT/RESOLUTION),(WIDTH/RESOLUTION)-2,(HEIGHT/RESOLUTION)-2])
            
            if grid[convert_coords(j,i)].south == False:
                pygame.draw.rect(WINDOW,BLACK,[j*(WIDTH/RESOLUTION),i*(HEIGHT/RESOLUTION),(WIDTH/RESOLUTION)-2,(HEIGHT/RESOLUTION)])
            if grid[convert_coords(j,i)].east == False:
                pygame.draw.rect(WINDOW,BLACK,[j*(WIDTH/RESOLUTION),i*(HEIGHT/RESOLUTION),(WIDTH/RESOLUTION),(HEIGHT/RESOLUTION)-2])
            
            if convert_coords(j,i) == stack[-1]:
                pygame.draw.rect(WINDOW,RED,[j*(WIDTH/RESOLUTION),i*(HEIGHT/RESOLUTION),(WIDTH/RESOLUTION)-2,(HEIGHT/RESOLUTION)-2])

def get_unv(index,grid):
    unv = []
    if index-RESOLUTION > 0 and grid[index-RESOLUTION].visited == False:
        unv.append(index-RESOLUTION)

    if (index+1)%RESOLUTION != 0 and grid[index+1].visited == False:
        unv.append(index+1)

    if index+RESOLUTION < RESOLUTION*RESOLUTION and grid[index+RESOLUTION].visited == False:
        unv.append(index+RESOLUTION)
    
    if index-1 > 0 and (index-1)%RESOLUTION != RESOLUTION-1 and grid[index-1].visited == False:
        unv.append(index-1)

    return unv

def main():
    run = True
    clock = pygame.time.Clock()
    
    unv = []
    grid = []
    stack = []
    num_vis = 0
    index = 0

    #fills grid with nodes
    for i in range(RESOLUTION*RESOLUTION):
        grid.append(node())

    stack.append(0)
    grid[0].visited = True
    num_vis += 1

    #main game loop
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        unv = get_unv(stack[-1],grid)
        if len(unv) != 0:
            index = random.choice(unv)

            if(index == stack[-1] + 1):
                grid[stack[-1]].east = False
            elif(index == stack[-1] + RESOLUTION):
                grid[stack[-1]].south = False
            elif(index == stack[-1] - RESOLUTION):
                grid[stack[-1] - RESOLUTION].south = False
            elif(index == stack[-1] - 1):
                grid[stack[-1] - 1].east = False
            #print(stack[-1] , grid[stack[-1]].east)

            stack.append(index)
            grid[index].visited = True
            num_vis += 1
        else:
            stack.pop()

        if num_vis == RESOLUTION * RESOLUTION:
            unv.clear()
            stack.clear()
            num_vis = 0
            index = 0

            #clear grid an reset vars for next run
            for i in range(RESOLUTION*RESOLUTION):
                grid[i].east = True
                grid[i].south = True
                grid[i].visited = False

            stack.append(0)
            grid[0].visited = True
            num_vis += 1 

        draw(grid,stack)
        pygame.display.update()

    pygame.quit

if __name__ == "__main__":
    main()