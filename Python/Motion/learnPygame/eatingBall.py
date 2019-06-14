
import pygame
from pygame import gfxdraw

import random
import numpy
import math


green = (0,255,0)
black = (0,0,0)
blue = (0,0,255)
height = 600
width = 600
boundary = 10



settings = {
    'max_vel': 10,
    'health': 100
}






def main():

    #Starting module:
    pygame.init()
    display = pygame.display.set_mode([height, width])
    clock = pygame.time.Clock()




    orgs = []
    food = []


    for i in range(5):
        orgs.append(Organism(settings, display, random.randrange(0,height), random.randrange(0,width)))

    running = True
    while(running):
        display.fill(black)

        if len(orgs) < 5 or random.random() < 0.0001:
            orgs.append(Organism(settings, display, random.randrange(0,height), random.randrange(0,width)))
        
        if len(food) < 15:
            food.append(numpy.array([random.uniform(0, width), random.uniform(0, height)], dtype='float64'))



        for org in orgs[::-1]:
            print(org.health)
            org.eat(food)
            org.boundaries()

            org.update()
            org.draw()

            if org.dead(food):
                orgs.remove(org)
                print("Organism died")
        


        for i in food:
            pygame.draw.circle(display, (0,0,225), [int(i[0]), int(i[1])], 3)
            
    
        pygame.display.update()
        clock.tick(60)

    pygame.quit()





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



class Organism:
    def __init__(self, settings, window, xpos, ypos):
        self.position = numpy.array([xpos,ypos], dtype='float64')
        self.velocity = numpy.array([random.uniform(-settings['max_vel'],settings['max_vel']),random.uniform(-settings['max_vel'],settings['max_vel'])], dtype='float64')
        self.acceleration = numpy.array([0, 0], dtype='float64')
        self.angle = 0 

        self.max_vel = 1.5
        self.max_force = .6
        self.color = green
        self.size = 6
        self.health = settings['health']

        self.window = window

    def apply_force(self, force):
        self.acceleration += force
    
    def find(self, target):
        desired_vel = numpy.add(target, -self.position)
        desired_vel = normalise(desired_vel)*self.max_vel

        steering_force = numpy.add(desired_vel, -self.velocity)
        steering_force = normalise(steering_force)*self.max_force
        
        return(steering_force)


    def eat(self, itemList):
        closest = None

        closest_distance = max(width, height)

        posx = self.position[0]
        posy = self.position[1]

        foodIndex = len(itemList)-1

        for i in itemList[::-1]:
            item_x = i[0]
            item_y = i[1]

            distance = math.hypot(posx-item_x, posy-item_y)

            if distance < 5:
                itemList.pop(foodIndex)
                self.health += 5

            if distance < closest_distance:
                closest_distance = distance
                closest = i
            foodIndex -= 1

        prey = self.find(closest)
        seek = normalise(prey)*self.max_force
        self.apply_force(seek)



    def update(self):
        self.velocity += self.acceleration
        self.velocity = normalise(self.velocity)*self.max_vel

        self.position += self.velocity
        self.acceleration *= 0
        self.health -= 0.2
        self.health = min(settings['health'], self.health)

    def draw(self):
        pygame.gfxdraw.aacircle(self.window, int(self.position[0]), int(self.position[1]), self.size, self.color)
        pygame.gfxdraw.filled_circle(self.window, int(self.position[0]), int(self.position[1]), self.size, self.color)

    def dead(self, itemList):
        if self.health > 0:
            return False
        else:
            if self.position[0] < width-boundary and self.position[0] > boundary and self.position[1] < height-boundary and self.position[1] > boundary:
                itemList.append(self.position)

            return True

    def boundaries(self):
            desired = None
            
            #if x value is on frame of boundary or visable window
            if self.position[0] < boundary:
                desired = numpy.array([self.max_vel, self.velocity[1]])
                steer = desired-self.velocity
                steer = normalise(steer)*self.max_force
                self.apply_force(steer)

            #if x value is larger than the window or outside
            elif self.position[0] > width - boundary:
                desired = numpy.array([-self.max_vel, self.velocity[1]])
                steer = desired-self.velocity
                steer = normalise(steer)*self.max_force
                self.apply_force(steer)
            #y value on boarder frame
            if self.position[1] < boundary:
                desired = numpy.array([self.velocity[0], self.max_vel])
                steer = desired-self.velocity
                steer = normalise(steer)*self.max_force
                self.apply_force(steer)
            # y value outside of window range
            elif self.position[1] > height - boundary:
                desired = numpy.array([self.velocity[0], -self.max_vel])
                steer = desired-self.velocity
                steer = normalise(steer)*self.max_force
                self.apply_force(steer)
            



if __name__ == '__main__':
    main()