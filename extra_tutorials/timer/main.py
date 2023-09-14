# Pygame Tutorial: Creating timers - Clear Code <3
# https://www.youtube.com/watch?v=YOCt8nsQqEo&t=2s&ab_channel=ClearCode
import pygame, sys

pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

current_time = 0
button_press_time = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if event.button == 1:
        #         button_press_time = pygame.time.get_ticks()
        #         screen.fill((255, 255, 255))
    clicks = pygame.mouse.get_pressed()

    if clicks[0]:
        button_press_time = pygame.time.get_ticks()
        screen.fill((255, 255, 255))

    current_time = pygame.time.get_ticks()

    if current_time - button_press_time > 2000:
        screen.fill((0, 0, 0))

    pygame.display.update()
    clock.tick(60)
