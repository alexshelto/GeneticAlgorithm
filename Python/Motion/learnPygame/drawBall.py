
import pygame

width = 600
height = 600
green = (0,255,0)
black = (0,0,0)

ballsize = 8

display = pygame.display.set_mode([width,height])
pygame.display.set_caption("Window Caption")


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.draw.circle(display,green, [width//2,height//2],ballsize)
    pygame.display.update()

pygame.quit()