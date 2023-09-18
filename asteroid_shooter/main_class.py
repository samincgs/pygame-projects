import pygame, sys


class Ship(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load("graphics/ship.png").convert_alpha()
        self.rect = self.image.get_rect(center=(screen_width / 2, screen_height / 2))


class Laser(pygame.sprite.Sprite):
    def __init__(self, groups, pos_x, pos_y):
        super().__init__(groups)
        self.image = pygame.image.load("graphics/laser.png").convert_alpha()
        self.rect = self.image.get_rect(center=(pos_x, pos_y))


pygame.init()

screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Asteroid Shooter")
clock = pygame.time.Clock()

# background
bg = pygame.image.load("graphics/background.png").convert()

# object calls
ship_group = pygame.sprite.GroupSingle()
ship = Ship(ship_group)

laser_group = pygame.sprite.Group()
laser = Laser(laser_group, 200, 60)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    dt = clock.tick() / 1000

    screen.blit(bg, (0, 0))

    ship_group.draw(screen)
    laser_group.draw(screen)

    pygame.display.update()
