# Asteroid Shooter Game created using functional programming.
import pygame, sys, random

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

# Meteor
meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 300)
meteor_surf = pygame.image.load("graphics/meteor.png").convert_alpha()
meteor_list = []
meteor_speed = 100

# Sounds
laser_sound = pygame.mixer.Sound("sounds/laser.ogg")
laser_sound.set_volume(0.1)
explosion_sound = pygame.mixer.Sound("sounds/explosion.wav")
explosion_sound.set_volume(0.1)
game_sound = pygame.mixer.Sound("sounds/music.wav")
game_sound.set_volume(0.1)
game_sound.play(loops=-1)


while True:
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and can_shoot:
            laser_sound.play()
            laser_rect = laser_surf.get_rect(midbottom=(ship_rect.midtop))
            laser_list.append(laser_rect)

            can_shoot = False
            shoot_time = pygame.time.get_ticks()

        if event.type == meteor_timer:
            x_pos = random.randint(-100, WINDOW_WIDTH + 100)
            y_pos = random.randint(-100, -50)
            meteor_rect = meteor_surf.get_rect(
                center=(
                    x_pos,
                    y_pos,
                )
            )

            direction = pygame.math.Vector2(random.uniform(-0.5, 0.5), 1)

            meteor_list.append((meteor_rect, direction))

    # mouse events
    # mouse = pygame.mouse.get_pressed()

    screen.blit(bg_surf, (0, 0))
    ship_rect.center = pygame.mouse.get_pos()

    if not can_shoot:
        current_time = pygame.time.get_ticks()
        if current_time - shoot_time > 300:
            can_shoot = True

    # dt
    dt = clock.tick(120) / 1000

    # collisions
    for meteor_tuple in meteor_list:
        meteor_rect = meteor_tuple[0]
        if ship_rect.colliderect(meteor_rect):
            pygame.quit()
            sys.exit()

    # laser meteor collision
    for laser in laser_list:
        for meteor_tuple in meteor_list:
            if laser_rect.colliderect(meteor_tuple[0]):
                laser_list.remove(laser)
                meteor_list.remove(meteor_tuple)
                explosion_sound.play()

    asteroid_msg = text_font.render(
        f"Score: {(pygame.time.get_ticks() // 1000)} ", True, (255, 255, 255)
    )
    asteroid_msg_rect = asteroid_msg.get_rect(center=(WINDOW_WIDTH / 2, 620))

    pygame.draw.rect(
        screen, "white", asteroid_msg_rect.inflate(30, 30), width=6, border_radius=10
    )
    screen.blit(asteroid_msg, asteroid_msg_rect)
    screen.blit(ship_surf, ship_rect)

    for laser in laser_list:
        screen.blit(laser_surf, laser)
        laser.y -= round(speed * dt)
        if laser.bottom < 0:
            laser_list.remove(laser)

    for meteor_tuple in meteor_list:
        meteor_rect = meteor_tuple[0]
        screen.blit(meteor_surf, meteor_rect)
        direction = meteor_tuple[1]
        meteor_rect.center += direction * speed * dt
        # meteor.y += round(meteor_speed * dt)
        if meteor_rect.top > WINDOW_HEIGHT:
            meteor_list.remove(meteor_tuple)

    pygame.display.update()
