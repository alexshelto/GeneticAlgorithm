


import json
import pygame
from pygame import gfxdraw

import random
import numpy
import math
from physics import normalise, magnitude_calc



with open('config.json') as config_file:
        settings = json.load(config_file)





class Organism:
    def __init__(self, settings, window, xpos, ypos):
        self.position = numpy.array([xpos,ypos], dtype='float64')
        self.velocity = numpy.array([random.uniform(-settings['organism']['max_vel'],settings['organism']['max_vel']),random.uniform(-settings['organism']['max_vel'],settings['organism']['max_vel'])], dtype='float64')
        self.acceleration = numpy.array([0, 0], dtype='float64')
        self.angle = 0 

        self.max_vel = settings['predator']['max_vel']
        self.max_force = .6
        self.color = settings['colors']['green']
        self.size = 6
        self.health = settings['organism']['health']

        self.window = window

    def apply_force(self, force):
        self.acceleration += force
    
    def find(self, target):
        desired_vel = numpy.add(target, -self.position)
        desired_vel = normalise(desired_vel)*self.max_vel

        steering_force = numpy.add(desired_vel, -self.velocity)
        steering_force = normalise(steering_force)*self.max_force
        
        return(steering_force)


    def eat(self,itemList, index):
        if index == 0:
            hp = 40
        else:
            hp = -30

        closest = None

        closest_distance = settings['pygame_settings']['window_width']

        posx = self.position[0]
        posy = self.position[1]

        foodIndex = len(itemList)-1

        for i in itemList[::-1]:
            item_x = i[0]
            item_y = i[1]

            distance = math.hypot(posx-item_x, posy-item_y)

            if distance < 5:
                itemList.pop(foodIndex)
                self.health += hp

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
        self.health = min(settings['organism']['health'], self.health)

    def draw(self):
        pygame.gfxdraw.aacircle(self.window, int(self.position[0]), int(self.position[1]), self.size, self.color)
        pygame.gfxdraw.filled_circle(self.window, int(self.position[0]), int(self.position[1]), self.size, self.color)

    def dead(self, itemList):
        if self.health > 0:
            return False
        else:
            if self.position[0] < settings['pygame_settings']['window_width']-settings['pygame_settings']['boundary'] and self.position[0] > settings['pygame_settings']['boundary'] and self.position[1] < settings['pygame_settings']['window_height']-settings['pygame_settings']['boundary'] and self.position[1] > settings['pygame_settings']['boundary']:
                itemList.append(self.position)

            return True

    def boundaries(self):
            desired = None
            
            #if x value is on frame of settings['pygame_settings']['boundary'] or visable window
            if self.position[0] < settings['pygame_settings']['boundary']:
                desired = numpy.array([self.max_vel, self.velocity[1]])
                steer = desired-self.velocity
                steer = normalise(steer)*self.max_force
                self.apply_force(steer)

            #if x value is larger than the window or outside
            elif self.position[0] > settings['pygame_settings']['window_width'] - settings['pygame_settings']['boundary']:
                desired = numpy.array([-self.max_vel, self.velocity[1]])
                steer = desired-self.velocity
                steer = normalise(steer)*self.max_force
                self.apply_force(steer)
            #y value on boarder frame
            if self.position[1] < settings['pygame_settings']['boundary']:
                desired = numpy.array([self.velocity[0], self.max_vel])
                steer = desired-self.velocity
                steer = normalise(steer)*self.max_force
                self.apply_force(steer)
            # y value outside of window range
            elif self.position[1] > settings['pygame_settings']['window_height'] - settings['pygame_settings']['boundary']:
                desired = numpy.array([self.velocity[0], -self.max_vel])
                steer = desired-self.velocity
                steer = normalise(steer)*self.max_force
                self.apply_force(steer)
            

