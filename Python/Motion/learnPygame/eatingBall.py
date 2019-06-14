
import pygame
from pygame import gfxdraw

import random
import numpy
import math


green = (0,255,0)
blue = (0,0,255)
height = 600
width = 600



settings = {}
settings['max_vel'] = 10







def main():

    #Starting module:
    pygame.init()
    display = pygame.display.set_mode([height, width])
    clock = pygame.time.Clock()


    orgs = []
    p0 = Organism(settings, display, random.randrange(0,height), random.randrange(0,width))

    orgs.append(p0)

    food = Food(display)

    stop = True
    while stop:
        display.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        for org in orgs:
            org.apply_force(food)
            org.update()
            org.draw()
            food.draw()

        pygame.display.update()
        clock.tick(60)





def magnitude_calc(vector):
    x = 0
    for i in vector:
        x += i**2
    magnitude = x**0.5
    return magnitude

def normalise(vector):
    magnitude = magnitude_calc(vector)
    if magnitude != 0:
        vector = vector / magnitude
    return vector




class Food:
    def __init__(self,window):
        self.window = window
        self.color = blue

    def draw(self):
        pygame.gfxdraw.aacircle(self.window, int(random.randrange(0,width)), int(random.randrange(0,height)), self.size, self.color)



class Organism:
    def __init__(self, settings, window, xpos, ypos):
        self.position = numpy.array([xpos,ypos], dtype='float64')
        self.velocity = numpy.array([random.uniform(-settings['max_vel'],settings['max_vel']),random.uniform(-settings['max_vel'],settings['max_vel'])], dtype='float64')
        self.acceleration = numpy.array([0, 0], dtype='float64')
        self.angle = 0 

        self.max_vel = 2
        self.max_force = .8
        self.color = green
        self.size = 8
        self.health = 100

        self.window = window

    def apply_force(self, force):
        self.acceleration += force
    
    def find(self, target):
        desired_vel = numpy.add(target, -self.position)
        desired_vel = normalise(desired_vel)*self.max_vel

        steering_force = numpy.add(desired_vel, -self.velocity)
        steering_force = normalise(steering_force)*self.max_force
        
        return(steering_force)

    def update(self):
        self.velocity += self.acceleration
        self.velocity = normalise(self.velocity)*self.max_vel

        self.position += self.velocity
        self.acceleration *= 0
        self.health -= 0.1

    def draw(self):
        pygame.gfxdraw.aacircle(self.window, int(self.position[0]), int(self.position[1]), self.size, self.color)





if __name__ == '__main__':
    main()