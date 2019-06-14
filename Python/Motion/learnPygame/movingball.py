


import pygame
from pygame import gfxdraw

import random
import numpy
import math


green = (0,255,0)
height = 600
width = 600



# Need to move circles around the window.
# Physics momentum
# orientation
# velocity, force, 
#
#

settings = {}
settings['max_vel'] = 10


def magnitude_calc(vector):
    x = 0
    for i in vector:
        x += i**2
    magnitude = x**0.5
    return(magnitude)

def normalise(vector):
    magnitude = magnitude_calc(vector)
    if magnitude != 0:
        vector = vector/magnitude
    return(vector)




def main():






    pygame.init()
    display = pygame.display.set_mode([width,height])
    pygame.display.set_caption("Window Caption")
    
    clock = pygame.time.Clock()
    balls = []


    b = Ball(random.randrange(0,width), random.randrange(0,height), display, settings)
    balls.append(b)

    stop = True
    while stop:
        display.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        for ball in balls:
            b.apply_force(ball.seek(pygame.mouse.get_pos()))
            ball.update()
            ball.draw()
        pygame.display.update()
        clock.tick(60)
    pygame.quit()


class Ball:
    def __init__(self, xpos, ypos, window, settings):
        self.position = numpy.array([xpos,ypos], dtype='float64')
        self.velocity = numpy.array([random.uniform(-settings['max_vel'],settings['max_vel']),random.uniform(-settings['max_vel'],settings['max_vel'])], dtype='float64')
        self.acceleration = numpy.array([0, 0], dtype='float64')
        self.angle = 0

        self.max_vel = 2
        self.max_force = 0.5
        self.color = green
        self.size = 8
        self.health = 100

        self.window = window
    

    def apply_force(self, force):
        self.acceleration += force
        

    
    def seek(self, target):
        desired_vel = numpy.add(target, -self.position)
        desired_vel = normalise(desired_vel)*self.max_vel
        steering_force = numpy.add(desired_vel, -self.velocity)
        steering_force = normalise(steering_force)*self.max_force
        return(steering_force)
        #self.apply_force(steering_force)


    def update(self):

        mouse_pos = pygame.mouse.get_pos()

        self.velocity += self.acceleration
        self.velocity = normalise(self.velocity)*self.max_vel
        self.position += self.velocity
        self.acceleration *= 0
        self.health -= 0.2



    def draw(self):
        pygame.gfxdraw.aacircle(self.window, int(self.position[0]), int(self.position[1]), self.size, self.color)








if __name__ == "__main__":
    main()