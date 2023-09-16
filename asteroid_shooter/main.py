import pygame, sys

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteroid Shooter")
clock = pygame.time.Clock()

# Images
bg_surf = pygame.image.load("graphics/background.png").convert()
ship_surf = pygame.image.load("graphics/ship.png").convert_alpha()
ship_rect = ship_surf.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

# Fonts
text_font = pygame.font.Font("graphics/subatomic.ttf", 40)
asteroid_msg = text_font.render("ASTEROID!", True, (255, 255, 255))
asteroid_msg_rect = asteroid_msg.get_rect(center=(WINDOW_WIDTH / 2, 120))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surf, (0, 0))
    screen.blit(ship_surf, ship_rect)
    screen.blit(asteroid_msg, asteroid_msg_rect)

    pygame.display.update()
    clock.tick(60)
