import pygame, sys

# Init
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteroid Shooter")
clock = pygame.time.Clock()

# Images
bg_surf = pygame.image.load("graphics/background.png").convert()
ship_surf = pygame.image.load("graphics/ship.png").convert_alpha()
ship_rect = ship_surf.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
laser_surf = pygame.image.load("graphics/laser.png").convert()
laser_rect = laser_surf.get_rect(midbottom=(ship_rect.midtop))


# Fonts
text_font = pygame.font.Font("graphics/subatomic.ttf", 40)
asteroid_msg = text_font.render("ASTEROID!", True, (255, 255, 255))
asteroid_msg_rect = asteroid_msg.get_rect(center=(WINDOW_WIDTH / 2, 120))


while True:
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # if event.type == pygame.MOUSEMOTION:
        #     ship_rect.center = event.pos
        # if event.type == pygame.MOUSEBUTTONUP:
        #     print(event.pos)

    # mouse events
    # mouse = pygame.mouse.get_pressed()
    # ship_rect.center = pygame.mouse.get_pos()

    laser_rect.y -= 7

    screen.blit(bg_surf, (0, 0))

    pygame.draw.rect(
        screen, "white", asteroid_msg_rect.inflate(30, 30), width=6, border_radius=10
    )
    screen.blit(asteroid_msg, asteroid_msg_rect)
    screen.blit(laser_surf, laser_rect)
    screen.blit(ship_surf, ship_rect)

    pygame.display.update()
    clock.tick(120)
