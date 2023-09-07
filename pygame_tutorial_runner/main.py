import pygame, sys

pygame.init() 

width = 800
height = 400


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tutorial Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()
text_surface = test_font.render("My game", False, "black"  )

snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(bottomleft = (600, 300))

player_surf = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
   
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    
        
    
    screen.blit(snail_surf, snail_rect)
    # snail_rect.x -=3
    # if snail_rect.right < 0: snail_rect.left = 800
    screen.blit(player_surf, player_rect )
    
    
    pygame.display.update()
    clock.tick(60)
