import pygame, sys, random


pygame.init()

width, height = 1280, 960
bg_color = pygame.Color("grey12")
light_grey = (200, 200, 200)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

ball = pygame.Rect(width / 2 - 15, height / 2 - 15, 30, 30)
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))

player = pygame.Rect(width - 20, height / 2 - 70, 10, 140)
player_speed = 7

opponent = pygame.Rect(10, height / 2 - 70, 10, 140)
opponent_speed = 7


def ball_animation():
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.bottom >= height or ball.top <= 0:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= width:
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


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
    global ball_speed_x, ball_speed_y
    ball.center = (width / 2, height / 2)
    ball_speed_x *= random.choice((1, -1))
    ball_speed_y *= random.choice((1, -1))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ball_animation()
    player_input()
    opponent_ai()

    screen.fill(bg_color)

    pygame.draw.aaline(screen, light_grey, (width / 2, 0), (width / 2, height))
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, "white", ball)

    pygame.display.update()
    clock.tick(60)
