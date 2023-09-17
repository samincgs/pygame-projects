import pygame, sys

# Init
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteroid Shooter")
clock = pygame.time.Clock()
speed = 700

# Images
bg_surf = pygame.image.load("graphics/background.png").convert()
ship_surf = pygame.image.load("graphics/ship.png").convert_alpha()
ship_rect = ship_surf.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
laser_surf = pygame.image.load("graphics/laser.png").convert()
laser_list = []
# laser_rect = laser_surf.get_frect(midbottom=(ship_rect.midtop))
can_shoot = True
shoot_time = None

# Fonts
text_font = pygame.font.Font("graphics/subatomic.ttf", 40)


while True:
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and can_shoot:
            laser_rect = laser_surf.get_rect(midbottom=(ship_rect.midtop))
            laser_list.append(laser_rect)

            can_shoot = False
            shoot_time = pygame.time.get_ticks()

    # mouse events
    # mouse = pygame.mouse.get_pressed()

    ship_rect.center = pygame.mouse.get_pos()

    if not can_shoot:
        current_time = pygame.time.get_ticks()
        if current_time - shoot_time > 300:
            can_shoot = True

    # dt
    dt = clock.tick(120) / 1000

    screen.blit(bg_surf, (0, 0))

    asteroid_msg = text_font.render(
        f"Score: {(pygame.time.get_ticks() // 1000)} ", True, (255, 255, 255)
    )
    asteroid_msg_rect = asteroid_msg.get_rect(center=(WINDOW_WIDTH / 2, 600))

    pygame.draw.rect(
        screen, "white", asteroid_msg_rect.inflate(30, 30), width=6, border_radius=10
    )
    print(can_shoot)
    screen.blit(asteroid_msg, asteroid_msg_rect)
    screen.blit(ship_surf, ship_rect)
    for laser in laser_list:
        screen.blit(laser_surf, laser)
        laser.y -= round(speed * dt)
        if laser.bottom < 0:
            laser_list.remove(laser)

    pygame.display.update()
