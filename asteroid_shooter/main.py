import pygame, sys

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteroid Shooter")
clock = pygame.time.Clock()

surf = pygame.Surface((120, 80))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surf.fill((255, 215, 0))
    screen.blit(surf, (500, 500))

    pygame.display.update()
    clock.tick(60)
