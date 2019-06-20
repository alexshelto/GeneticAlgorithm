


import json
import pygame
from pygame import gfxdraw

import random
import numpy
import math

from physics import normalise, magnitude_calc



with open('config.json') as config_file:
        settings = json.load(config_file)



#    DNA
# DNA[0] = max force , DNA[1]= steering weight , DNA[2] = perception
#
#

DNA = {
    'color': ,
    'speed_multiplier', 
    'health_bonus'    ,
    'steering_weights',
    'max_force'       ,
    'perception_mutation' ,
    'reproduction_rate:', 

}




class Organism:
    def __init__(self, settings, window, xpos, ypos, dna=False):
        self.position = numpy.array([xpos,ypos], dtype='float64')
        self.velocity = numpy.array([random.uniform(-settings['organism']['max_vel'],settings['organism']['max_vel']),random.uniform(-settings['organism']['max_vel'],settings['organism']['max_vel'])], dtype='float64')
        self.acceleration = numpy.array([0, 0], dtype='float64')
        self.angle = 0 

        self.max_vel = settings['organism']['max_vel']
        self.max_force = settings['organism']['max_force']
        self.color = settings['colors']['green']
        self.size = 6
        self.health = settings['organism']['health']

        self.window = window

        self.fitness = 0


        if dna == False:
            self.dna = {}
            

        if dna != False:
            self.dna = []
            for gene in range(len(dna)):
                if random.random() < settings['organism']['reproduction_rate']:
                    if gene < 2:
                        self.dna.append(dna[gene]+ random.uniform(-settings['organism_mutation']['steering_weight'],settings['organism_mutation']['steering_weight'] ))
                    else:
                        self.dna.append(dna[gene] + random.uniform(-settings['organism_mutation']['perception_mutation'],settings['organism_mutation']['perception_mutation'] ))
                else:
                    self.dna.append(dna[gene])
        else: #load with random dna
            self.dna = [random.uniform(-settings['organism']['max_force'],settings['organism']['max_force']),
            random.uniform(-settings['organism']['max_force'],settings['organism']['max_force']),random.uniform(0,settings['organism']['perception_radius']), random.uniform(0, settings['organism']['perception_radius'])]
            print(self.dna)



    def reproduce(self, orgList):
        if random.random() < settings['organism']['reproduction_rate']:
            orgList.append(Organism(settings, self.window,self.position[0], self.position[1],self.dna))
            print("reproduction")
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

        if closest_distance < self.dna[2]:
            prey = self.find(closest)
            prey *= self.dna[index]
            seek = normalise(prey)*self.max_force
            self.apply_force(seek)



    def update(self):
        self.velocity += self.acceleration
        self.velocity = normalise(self.velocity)*self.max_vel

        self.position += self.velocity 
        self.acceleration *= 0 #resets acceleration to 0
        self.health -= 0.2
        self.health = min(settings['organism']['health'], self.health)

        self.fitness += 1

    def draw(self):
        ## Shape of organism
        pygame.gfxdraw.aacircle(self.window, int(self.position[0]), int(self.position[1]), self.size, self.color)
        pygame.gfxdraw.filled_circle(self.window, int(self.position[0]), int(self.position[1]), self.size, self.color)

        #Visual Atributes:
        #food and poison range:
        pygame.draw.circle(self.window, settings['colors']['red'], (int(self.position[0]), int(self.position[1])), abs(int(self.dna[3])), abs(int(min(2, self.dna[3]))))
        pygame.draw.circle(self.window, settings['colors']['green'], (int(self.position[0]), int(self.position[1])), abs(int(self.dna[2])), abs(int(min(2, self.dna[2]))))

        #Speed:



        # pygame.gfxdraw.aacircle(self.window,int(self.position[0]), int(self.position[1]),abs(int(self.dna[2])), settings['colors']['white'])
        # pygame.gfxdraw.aacircle(self.window,int(self.position[0]), int(self.position[1]),abs(int(self.dna[0])), settings['colors']['yellow'] )

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
            

    def returnFitness(self):
        pass
        #clock = 
        #return self.timeAlive (secs)