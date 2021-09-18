import random
import time
import pygame

windowSize = (1000,1000)

white = (255,255,255)
black = (0,0,0)
grey = (128,128,128)
resolution = 10

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
            #print(i)
            for j in range(self.size):
                #print(j)
                self.grid.append(node(i,j))

    def get_grid(self):
        return self.grid

    def draw(self):
        for i in range(self.size):
            for j in range(self.size):
                print('--')

pygame.init

m = maze(resolution)
m.setup()
print(len(m.grid))
