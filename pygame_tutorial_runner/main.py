import pygame, sys

pygame.init() 

width = 800
height = 400
fps = 60

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tutorial Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()
text_surface = test_font.render("My game", False, "black"  )

snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_x_pos = 600

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
   
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    snail_x_pos-=3
    if snail_x_pos + snail_surface.get_width() < 0:
        snail_x_pos = 800
    screen.blit(snail_surface, (snail_x_pos, 250))
    
    pygame.display.update()
    clock.tick(fps)
