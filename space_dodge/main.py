import pygame, sys
import time, random

pygame.init()

width, height = 1000, 800
spaceship_width, spaceship_height = 120, 80
spaceship_velocity = 5
start_time = time.time()
elapsed_time = 0
# left_pressed = False
# right_pressed = False

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Dodge")
clock = pygame.time.Clock()
font = pygame.font.Font("fonts/20thcenturyfont.ttf", 35)

# WALLPAPER
wallpaper = pygame.transform.scale(
    pygame.image.load("images/wallpaper.jpg"), (width, height)
).convert()

# SPACESHIP
spaceship_surf = pygame.transform.scale(
    pygame.image.load("images/spaceship.png"), (spaceship_width, spaceship_height)
).convert_alpha()
spaceship_rect = spaceship_surf.get_rect(midbottom=(width / 2, height))

run = True

while run:
    elapsed_time = time.time() - start_time

    # TEXT
    game_text = font.render(f"Time: {round(elapsed_time)}", False, "white")
    game_text_rect = game_text.get_rect(topleft=(10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         left_pressed = True
        #     if event.key == pygame.K_RIGHT:
        #         right_pressed = True

        # if event.type == pygame.KEYUP:
        #     left_pressed = False
        #     right_pressed = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and spaceship_rect.left >= 0:
        spaceship_rect.x -= spaceship_velocity
    if keys[pygame.K_RIGHT] and spaceship_rect.right <= width:
        spaceship_rect.x += spaceship_velocity

    screen.blit(wallpaper, (0, 0))
    screen.blit(spaceship_surf, spaceship_rect)
    screen.blit(game_text, game_text_rect)

    pygame.display.update()
    clock.tick(60)
