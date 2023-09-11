import pygame, sys

pygame.init()

width, height = 1280, 960
bg_color = pygame.Color("grey12")
light_grey = (200, 200, 200)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

ball = pygame.Rect(width / 2 - 15, height / 2 - 15, 30, 30)
player = pygame.Rect(width - 20, height / 2 - 70, 10, 140)
opponent = pygame.Rect(10, height / 2 - 70, 10, 140)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(bg_color)

    pygame.draw.aaline(screen, light_grey, (width / 2, 0), (width / 2, height))
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, "white", ball)

    pygame.display.update()
    clock.tick(60)
