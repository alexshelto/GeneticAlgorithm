


import pygame
from pygame import gfxdraw

import random



green = (0,255,0)
height = 600
width = 600




def main():
    pygame.init()
    display = pygame.display.set_mode([width,height])
    pygame.display.set_caption("Window Caption")
    
    b = Ball(random.randrange(0,width), random.randrange(0,height), display)
    b.addBall()

    stop = True
    while stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        

        pygame.display.update()
    pygame.quit()


class Ball:
    def __init__(self, xpos, ypos, window):
        self.position = [xpos,ypos]
        self.velocity = 1

        self.color = green
        self.size = 8
        self.health = 100

        self.window = window

    def addBall(self):
        pygame.gfxdraw.aacircle(self.window, int(self.position[0]), int(self.position[1]), self.size, self.color)








if __name__ == "__main__":
    main()