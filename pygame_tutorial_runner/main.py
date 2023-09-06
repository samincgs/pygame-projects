import pygame, sys

pygame.init() 

width = 800
height = 400
fps = 60

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tutorial Runner")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # draw all our elements
    # update everything
    
    
    
    pygame.display.update()
    clock.tick(fps)
