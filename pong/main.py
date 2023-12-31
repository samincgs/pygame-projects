import pygame, sys, random

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

width, height = 1280, 960
bg_color = pygame.Color("grey12")
light_grey = (200, 200, 200)
font = pygame.font.Font(None, 40)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
score_time = True

ball = pygame.Rect(width / 2 - 15, height / 2 - 15, 30, 30)
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))

player = pygame.Rect(width - 20, height / 2 - 70, 10, 140)
player_speed = 7
player_score = 0

opponent = pygame.Rect(10, height / 2 - 70, 10, 140)
opponent_speed = 7
opponent_score = 0

pong_sound = pygame.mixer.Sound("sounds/pong.ogg")
score_sound = pygame.mixer.Sound("sounds/score.ogg")


def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.bottom >= height or ball.top <= 0:
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_y *= -1

    if ball.left <= 0:
        pygame.mixer.Sound.play(score_sound)
        player_score += 1
        score_time = pygame.time.get_ticks()

    if ball.right >= width:
        pygame.mixer.Sound.play(score_sound)
        opponent_score += 1
        score_time = pygame.time.get_ticks()

    if ball.colliderect(player) and ball_speed_x > 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.right - player.left) < 10:
            ball_speed_x *= -1
        elif abs(ball.top - player.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1
        elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1

    if ball.colliderect(opponent) and ball_speed_x < 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.left - opponent.right) < 10:
            ball_speed_x *= -1
        elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1
        elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1


def player_input():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN] and player.bottom <= height:
        player.y += player_speed
    if keys[pygame.K_UP] and player.top >= 0:
        player.y -= player_speed


def opponent_ai():
    if opponent.top < ball.y:
        opponent.y += opponent_speed
    if opponent.bottom > ball.y:
        opponent.y -= opponent_speed


def ball_restart():
    global ball_speed_x, ball_speed_y, score_time

    current_time = pygame.time.get_ticks()
    ball.center = (width / 2, height / 2)

    if current_time - score_time < 700:
        countdown_three = font.render("3", False, "red")
        screen.blit(countdown_three, (width / 2 - 7, height / 2 - 70))
    if 700 < current_time - score_time < 1400:
        countdown_two = font.render("2", False, "red")
        screen.blit(countdown_two, (width / 2 - 7, height / 2 - 70))
    if 1400 < current_time - score_time < 2100:
        countdown_one = font.render("1", False, "red")
        screen.blit(countdown_one, (width / 2 - 7, height / 2 - 70))

    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0, 0
    else:
        ball_speed_x = 7 * random.choice((1, -1))
        ball_speed_y = 7 * random.choice((1, -1))
        score_time = None


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ball_animation()
    player_input()
    opponent_ai()

    screen.fill(bg_color)

    score_text = font.render(f"{ player_score}", False, light_grey)
    score_text_opponent = font.render(f"{opponent_score}", False, light_grey)

    screen.blit(score_text, (width / 2 + 30, height / 2))
    screen.blit(score_text_opponent, (width / 2 - 50, height / 2))

    pygame.draw.aaline(screen, light_grey, (width / 2, 0), (width / 2, height))
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, "white", ball)

    if score_time:
        ball_restart()

    pygame.display.update()
    clock.tick(60)
