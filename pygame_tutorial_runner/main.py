import pygame, sys
from random import randint

pygame.init()

width = 800
height = 400
text_color = (64, 64, 64)
bg_text_color = (192, 232, 236)
bg_restart_game = (94, 129, 162)
game_active = False
start_time = 0
score = 0

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tutorial Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

# Obstacles
snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
fly_surf = pygame.image.load("graphics/Fly/Fly1.png").convert_alpha()

obstacle_rect_list = []

player_walk_1 = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_walk_2 = pygame.image.load("graphics/Player/player_walk_2.png").convert_alpha()
player_jump = pygame.image.load("graphics/Player/jump.png").convert_alpha()
player_stand = pygame.transform.scale2x(
    pygame.image.load("graphics/Player/player_stand.png")
).convert_alpha()
player_stand_rect = player_stand.get_rect(center=(width / 2, height / 2))

player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_gravity = 0


def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surf = test_font.render(f"Score: {current_time // 1000}", False, text_color)
    score_rect = score_surf.get_rect(center=(width / 2, 50))
    screen.blit(score_surf, score_rect)
    return current_time


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacles_rect in obstacle_list:
            obstacles_rect.x -= 6

            if obstacles_rect.bottom == 300:
                screen.blit(snail_surf, obstacles_rect)
            else:
                screen.blit(fly_surf, obstacles_rect)

            obstacle_list = [
                obstacle for obstacle in obstacle_list if obstacle.x > -100
            ]
        return obstacle_list
    else:
        return []


def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True


def player_animation():
    global player_surf, player_index
    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]


game_name = test_font.render("Pixel Runner", False, bg_text_color)
game_name_rect = game_name.get_rect(center=(width / 2, height / 5))
text_instruction = test_font.render("Press space to play", False, bg_text_color)
text_instruction_rect = text_instruction.get_rect(center=(width / 2, 335))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1000)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # PLAYER OPTIONS TO JUMP
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()

        if event.type == obstacle_timer and game_active:
            if randint(0, 2):
                obstacle_rect_list.append(
                    snail_surf.get_rect(bottomright=(randint(900, 1100), 300))
                )
            else:
                obstacle_rect_list.append(
                    fly_surf.get_rect(bottomright=(randint(900, 1100), 210))
                )

    if game_active:
        # Map
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        # Score
        score = display_score() // 1000
        # pygame.draw.rect(
        #     screen,
        #     bg_text_color,
        #     score_rect,
        # )
        # screen.blit(score_surf, score_rect)

        # Snail
        # screen.blit(snail_surf, snail_rect)
        # snail_rect.x -= 5
        # if snail_rect.right < 0:
        #     snail_rect.left = 800

        # Obstacle Movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        game_active = collisions(player_rect, obstacle_rect_list)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300

        player_animation()
        screen.blit(player_surf, player_rect)

        # state management
        # if player_rect.colliderect(snail_rect):
        #     game_active = False
    else:
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0
        screen.fill(bg_restart_game)
        screen.blit(player_stand, player_stand_rect)

        score_message = test_font.render(f"Score: {score}", False, bg_text_color)
        score_message_rect = score_message.get_rect(center=(width / 2, 335))
        screen.blit(game_name, game_name_rect)

        if score == 0:
            screen.blit(text_instruction, text_instruction_rect)
        else:
            screen.blit(score_message, score_message_rect)

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
