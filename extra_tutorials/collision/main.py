# Pygame tutorial: Collisions between static and moving objects - Clear Code <3
# https://www.youtube.com/watch?v=1_H7InPMjaY&ab_channel=ClearCode
import pygame, sys


def bouncing_rect():
    global x_speed, y_speed, other_speed

    moving_rect.x += x_speed
    moving_rect.y += y_speed

    # collision with screen borders
    if moving_rect.right >= 800 or moving_rect.left <= 0:
        x_speed *= -1
    if moving_rect.bottom >= 800 or moving_rect.top <= 0:
        y_speed *= -1

    # moving the other rectangle
    other_rect.y -= other_speed

    if other_rect.top <= 0 or other_rect.bottom >= 800:
        other_speed *= -1

    # collision with red rect
    if moving_rect.colliderect(other_rect):
        if abs(other_rect.top - moving_rect.bottom) < 10 and y_speed > 0:
            y_speed *= -1
        if abs(other_rect.bottom - moving_rect.top) < 10 and y_speed < 0:
            y_speed *= -1

        if abs(other_rect.right - moving_rect.left) < 10 and x_speed < 0:
            x_speed *= -1

        if abs(other_rect.left - moving_rect.right) < 10 and x_speed > 0:
            x_speed *= -1

    pygame.draw.rect(screen, "white", moving_rect)
    pygame.draw.rect(screen, "red", other_rect)


pygame.init()

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

moving_rect = pygame.Rect(350, 350, 100, 100)
x_speed, y_speed = 5, 4

other_rect = pygame.Rect(300, 600, 200, 100)
other_speed = 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((30, 30, 30))

    bouncing_rect()

    pygame.display.update()
    clock.tick(60)
