import pygame, sys
from random import randint, choice

pygame.init()

# VARIABLES
width = 800
height = 400
text_color = (64, 64, 64)
bg_text_color = (192, 232, 236)
bg_restart_game = (94, 129, 162)
game_active = False
start_time = 0
score = 0
obstacle_rect_list = []

# BASICS
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tutorial Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

# BACKGROUND
sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

# OBSTACLES

# SNAIL
snail_frame_1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_frame_2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_index = 0
snail_surf = snail_frames[snail_index]

# FLY
fly_frame_1 = pygame.image.load("graphics/Fly/Fly1.png").convert_alpha()
fly_frame_2 = pygame.image.load("graphics/Fly/Fly2.png").convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_index = 0
fly_surf = fly_frames[fly_index]


# PLAYER IMAGES
player_walk_1 = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_walk_2 = pygame.image.load("graphics/Player/player_walk_2.png").convert_alpha()
player_jump = pygame.image.load("graphics/Player/jump.png").convert_alpha()
player_stand = pygame.transform.scale2x(
    pygame.image.load("graphics/Player/player_stand.png")
).convert_alpha()
player_stand_rect = player_stand.get_rect(center=(width / 2, height / 2))

# PLAYER VARIABLES
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_gravity = 0


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load(
            "graphics/Player/player_walk_1.png"
        ).convert_alpha()
        player_walk_2 = pygame.image.load(
            "graphics/Player/player_walk_2.png"
        ).convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load("graphics/Player/jump.png").convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -17
        if mouse[0] and self.rect.bottom >= 300:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.gravity = -17

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation()


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == "fly":
            fly_1 = pygame.image.load("graphics/Fly/Fly1.png").convert_alpha()
            fly_2 = pygame.image.load("graphics/Fly/Fly2.png").convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210
        else:
            snail_1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
            snail_2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 7
        self.destroy_extra_sprites()

    def destroy_extra_sprites(self):
        if self.rect.x <= -100:
            self.kill()


player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle = pygame.sprite.Group()


# FUNCTIONS
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


def collision_sprites():
    if pygame.sprite.spritecollide(player.sprite, obstacle, False):
        obstacle.empty()
        return False
    else:
        return True


# def player_animation():
#     global player_surf, player_index
#     if player_rect.bottom < 300:
#         player_surf = player_jump
#     else:
#         player_index += 0.1
#         if player_index >= len(player_walk):
#             player_index = 0
#         player_surf = player_walk[int(player_index)]


# TEXT
game_name = test_font.render("Pixel Runner", False, bg_text_color)
game_name_rect = game_name.get_rect(center=(width / 2, height / 5))
text_instruction = test_font.render("Press space to play", False, bg_text_color)
text_instruction_rect = text_instruction.get_rect(center=(width / 2, 335))

# TIMERS
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 800)
snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)
fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # PLAYER OPTIONS TO JUMP
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -15

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20

        # GAME RESTART
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()

        # ADD OBSTACLES
        if game_active:
            if event.type == obstacle_timer:
                obstacle.add(Obstacle(choice(["fly", "snail", "snail", "snail"])))
                # if randint(0, 2):
                #     obstacle_rect_list.append(
                #         snail_surf.get_rect(bottomright=(randint(900, 1100), 300))
                #     )
                # else:
                #     obstacle_rect_list.append(
                #         fly_surf.get_rect(bottomright=(randint(900, 1100), 210))
                #     )

            # if event.type == snail_animation_timer:
            #     if snail_index == 0:
            #         snail_index = 1
            #     else:
            #         snail_index = 0
            # snail_surf = snail_frames[snail_index]

            # if event.type == fly_animation_timer:
            #     if fly_index == 0:
            #         fly_index = 1
            #     else:
            #         fly_index = 0
            #     fly_surf = fly_frames[fly_index]

    if game_active:
        # MAP
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        # SCORE
        score = display_score() // 1000

        # OBSTACLE MOVEMENT
        # obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        game_active = collisions(player_rect, obstacle_rect_list)

        # PLAYER
        # player_gravity += 1
        # player_rect.y += player_gravity
        # if player_rect.bottom >= 300:
        #     player_rect.bottom = 300

        # player_animation()
        # screen.blit(player_surf, player_rect)
        player.draw(screen)
        player.update()

        obstacle.draw(screen)
        obstacle.update()

        game_active = collision_sprites()

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
