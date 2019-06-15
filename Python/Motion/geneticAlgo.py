# Alexander Shelton
#


import organism
import predator

import pygame
from pygame import gfxdraw

import random
import numpy
import math
import json



#TODO make a timer, add dna, add fitness


#ORGANISM DNA: speed, force, health,  Vision distance, steering ,?cooperative, shoot?

#PREDATOR DNA: speed, strength, steering, vision 

#fix nonetype & float in find: desired val var


#---------------Functions ----------------------------------------------------------------+



def main():



    with open('config.json') as config_file:
        settings = json.load(config_file)

    #Starting module:
    pygame.init()
    display = pygame.display.set_mode([settings['pygame_settings']['window_height'],settings['pygame_settings']['window_width']])
    clock = pygame.time.Clock()

   


    orgs = []
    predators = []
    food = []
    poison = []

    for i in range(40):
        food.append(numpy.array([random.uniform(0, settings['pygame_settings']['window_width']), random.uniform(0, settings['pygame_settings']['window_height'])], dtype='float64'))   
    for i in range(8):
        orgs.append(organism.Organism(settings, display, random.randrange(0,settings['pygame_settings']['window_height']), random.randrange(0,settings['pygame_settings']['window_width'])))
        predators.append(predator.Predator(settings, display, random.randrange(0,settings['pygame_settings']['window_height']), random.randrange(0,settings['pygame_settings']['window_width'])))
        food.append(numpy.array([random.uniform(0, settings['pygame_settings']['window_width']), random.uniform(0, settings['pygame_settings']['window_height'])], dtype='float64'))   
        poison.append((numpy.array([random.uniform(0, settings['pygame_settings']['window_width']), random.uniform(0, settings['pygame_settings']['window_height'])], dtype='float64')))
    running = True
    while(running):
        display.fill(settings['colors']['black'])

        if random.random()<0.01:
            poison.append(numpy.array([random.uniform(0, settings['pygame_settings']['window_width']), random.uniform(0, settings['pygame_settings']['window_height'])], dtype='float64'))

        if len(orgs) < 5 or random.random() < 0.0001:
            orgs.append(organism.Organism(settings, display, random.randrange(0,settings['pygame_settings']['window_height']), random.randrange(0,settings['pygame_settings']['window_width'])))
        
        if len(food) < 50:
            food.append(numpy.array([random.uniform(0, settings['pygame_settings']['window_width']), random.uniform(0, settings['pygame_settings']['window_height'])], dtype='float64'))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        for org in orgs[::-1]:
            # print(org.health)
            org.eat(food,0)
            org.eat(poison,1)
            org.boundaries()

            org.update()
            org.draw()

            if org.dead(food):
                orgs.remove(org)
                print("Organism died")
            else:
                org.reproduce(orgs)
        
        for pred in predators[::-1]:
            pred.fight(orgs)
            pred.boundaries()

            pred.update()
            pred.draw()


        for i in food:
            pygame.draw.circle(display, (0,0,225), [int(i[0]), int(i[1])], 3)
            
        for i in poison:
            pygame.draw.circle(display, (122,4,233),[int(i[0]), int(i[1])], 3)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()




## Program

if __name__ == '__main__':
    main()








