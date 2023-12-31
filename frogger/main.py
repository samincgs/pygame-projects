import pygame, sys
from settings import *
from player import Player
from car import Car


class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def customize_draw(self):
        for sprite in self.sprites():
            screen.blit(sprite.image, sprite.rect)


pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Frogger")
clock = pygame.time.Clock()

# groups
all_sprites = AllSprites()

# classes
player = Player(all_sprites, (200, 300))
car = Car(all_sprites, (700, 400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # keyboard alternative
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_w:
        #         print("w")

    dt = clock.tick() / 1000

    screen.fill("black")

    all_sprites.update(dt)

    all_sprites.draw(screen)

    pygame.display.update()
