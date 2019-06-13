# Alexander Shelton
#
#
#
import pygame
from pygame.locals import *
from pygame import gfxdraw

import time
import random
import math
import numpy


#-------------- Constants ---------------------------------------------------------------+
#Window Settings:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
fps=60
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
BALL_SIZE = 10


settings = {}
#Evolution Settings:
settings['population_size'] = 100  #Number of organisms
settings['food_num'] = 200         #Number of food entities on screen
settings['generations'] = 100      #Number of generations
settings['mutation_rate'] = 0.10   #Rate at which organisms mutate
settings['size'] = 5
settings['health'] = 100

#Simulation Settings:
settings['generation_time'] = 100  #Generation length (Seconds)
settings['dt'] = 0.04              #Time step
settings['v_max'] = 0.5            #Max Velocity

#---------------Functions ----------------------------------------------------------------+








#--------------------- Classes -----------------------------------------------------------+

class Organism():
    def __init__(self, dna=False):
        self.position = numpy.array([random.randrange(0,SCREEN_WIDTH), random.randrange(0,SCREEN_HEIGHT)])

        self.color = BLUE
        self.health = 100
        self.max_vel = 3
        self.size = 5
        self.age = 1




#-------------------- Main ----------------------------------------------------------------+





## Program

if __name__ == '__main__':
    main()
