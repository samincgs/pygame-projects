import pygame, sys
from settings import *
from player import Player

# basic setup
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Frogger")
clock = pygame.time.Clock()

# groups
all_sprites = pygame.sprite.Group()

# sprites
player = Player((600, 400), all_sprites)

# game loop
while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # # keyboard input (method 1)
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_a:
        #         print("a")

        # (method 2)
        # keys = pygame.key.get_pressed()

    # delta time
    dt = clock.tick() / 1000

    # draw a bg
    display_surface.fill("black")

    # update
    all_sprites.update(dt)

    # draw
    all_sprites.draw(display_surface)

    pygame.display.update()
