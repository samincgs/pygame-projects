import pygame, sys


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface((width / 2, height / 2))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)


pygame.init()

width, height = 900, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


player_group = pygame.sprite.Group()
player = Player(100, 100)

player_group.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    player_group.draw(screen)

    pygame.display.update()
    clock.tick(60)
