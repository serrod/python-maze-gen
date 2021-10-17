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
RESOLUTION = 50

FPS = 120

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
            
            if grid[convert_coords(j,i)].south == False:
                pygame.draw.rect(WINDOW,BLACK,[j*(WIDTH/RESOLUTION),i*(HEIGHT/RESOLUTION),(WIDTH/RESOLUTION)-2,(HEIGHT/RESOLUTION)])
            if grid[convert_coords(j,i)].east == False:
                pygame.draw.rect(WINDOW,BLACK,[j*(WIDTH/RESOLUTION),i*(HEIGHT/RESOLUTION),(WIDTH/RESOLUTION),(HEIGHT/RESOLUTION)-2])

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

    for i in range(RESOLUTION):
            for j in range(RESOLUTION):
                grid.append(node(j,i))

    stack.append(0)
    grid[0].visited = True
    num_vis += 1

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        if len(stack) == 0:
            #end somehow
            print("end")

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

        draw(grid)
        pygame.display.update()

    pygame.quit

if __name__ == "__main__":
    main()