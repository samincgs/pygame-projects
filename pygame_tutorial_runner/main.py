import pygame, sys

pygame.init()

width = 800
height = 400
bg_text_color = (192, 232, 236)


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tutorial Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

score_surf = test_font.render("Score: ", False, (64, 64, 64))
score_rect = score_surf.get_rect(center=(width / 2, height / 2 - 150))

snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(bottomleft=(600, 300))

player_surf = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # PLAYER OPTIONS TO JUMP
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                player_gravity = -20
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                player_gravity = -20

    # Map
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))

    # Score
    pygame.draw.rect(
        screen,
        bg_text_color,
        score_rect,
    )
    pygame.draw.rect(screen, bg_text_color, score_rect, 10)
    screen.blit(score_surf, score_rect)

    # Snail
    screen.blit(snail_surf, snail_rect)
    snail_rect.x -= 3
    if snail_rect.right < 0:
        snail_rect.left = 800

    # Player
    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 300:
        player_rect.bottom = 300
    screen.blit(player_surf, player_rect)

    pygame.display.update()
    clock.tick(60)

    # OTHER SHAPES THAT CAN BE DRAWN
    # pygame.draw.line(screen, "black", (0, 0), (800,400))
    # pygame.draw.ellipse(screen, "aqua", pygame.Rect(50, 200, 20, 20))

    # ALTERNATIVE FOR KEY PRESSED
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print("jump")

    # ALTERNATIVE FOR MOUSE CLICK
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint((mouse_pos)):
    #     print("hit")
