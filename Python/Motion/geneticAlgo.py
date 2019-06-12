# Alexander Shelton
#
#
#
import pygame
from pygame.locals import *

import time 
import random
import math
import numpy

# ## Colors 
# white = (255,255,255)
# black = (0,0,0,)
# red = (255,0,0)
# green = (0,255,0)
# blue = (0,0,255)

# fps = 60



class Organism(Ball):
    def __init__(self, setUp):
        #Position of x and y
        self.x = uniform(setUp['x_min'], setUp['x_max'])
        self.y = uniform(setUp['y_min'], setUp['y_max'])
        
        self.orientation = uniform(0,360)
        self.velocity = uniform(setUp['v_max'])
        self.dv = uniform(setUp['dv_max'])

        self.distance_food = 100 #distance to the nearest food
        self.orientation_food = 0 #orientation to nearest food
        self. fintess = 0 #fitness, food count




# class Food():
#     def __init__(self, setUp):
#         self.x = uniform(setUp['x_min'], setUp['x_max'])
#         self.y = uniform(setUp['y_min'], setUp['y_max'])
#         self.energy = 1 #how much energy it gives

#     def respawn(self,setUp):
#         self.x = uniform(setUp['x_min'], setUp['x_max'])
#         self.y = uniform(setUp['y_min'], setUp['y_max'])
#         self.energy = 1
        
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BALL_SIZE = 25




class Ball:
    """
    Class to keep track of a ball's location and vector.
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        
 
 
def make_ball():
    """
    Function to make a new, random ball.
    """
    ball = Ball()
    # Starting position of the ball.
    # Take into account the ball size so we don't spawn on the edge.
    ball.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
    ball.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)
 
    # Speed and direction of rectangle
    ball.change_x = random.randrange(-2, 3)
    ball.change_y = random.randrange(-2, 3)
 
    return ball
 


class Organism(Ball):
    def __init__(self, setUp):
        #Position of x and y
        self.x = uniform(setUp['x_min'], setUp['x_max'])
        self.y = uniform(setUp['y_min'], setUp['y_max'])
        
        self.orientation = uniform(0,360)
        self.velocity = uniform(setUp['v_max'])
        self.dv = uniform(setUp['dv_max'])

        self.distance_food = 100 #distance to the nearest food
        self.orientation_food = 0 #orientation to nearest food
        self. fintess = 0 #fitness, food count

















 
def main():
    #creating the main page
    pygame.init()
    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Genetic Algorithim")
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    ball_list = []
 
    ball = make_ball()
    ball_list.append(ball)
 
    # -------- Main Program Loop -----------
    while not done:
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:#for key proess
                # Space bar! Spawn a new ball.
                if event.key == pygame.K_SPACE: #eventually change to pause
                    pause(screen)
                    ball = make_ball()
                    ball_list.append(ball)
 
        # --- Logic
        for ball in ball_list:
            # Move the ball's center
            ball.x += ball.change_x
            ball.y += ball.change_y
 
            # Bounce the ball if needed
            if ball.y > SCREEN_HEIGHT - BALL_SIZE or ball.y < BALL_SIZE:
                ball.change_y *= -1
            if ball.x > SCREEN_WIDTH - BALL_SIZE or ball.x < BALL_SIZE:
                ball.change_x *= -1
 
        # --- Drawing
        # Set the screen background
        screen.fill(BLACK)
        # Draw the balls
        for ball in ball_list:
            pygame.draw.circle(screen, WHITE, [ball.x, ball.y], BALL_SIZE)
        # --- Wrap-up
        # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()








def pause(screen):
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        screen.fill(WHITE)
    
        pygame.display.update()
 


 #Running the program
if __name__ == "__main__":
    main()
