import pygame, sys


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load("frog_images/frog_1.png"))
        self.sprites.append(pygame.image.load("frog_images/frog_2.png"))
        self.sprites.append(pygame.image.load("frog_images/frog_3.png"))
        self.sprites.append(pygame.image.load("frog_images/frog_4.png"))
        self.sprites.append(pygame.image.load("frog_images/frog_5.png"))
        self.sprites.append(pygame.image.load("frog_images/frog_6.png"))
        self.sprites.append(pygame.image.load("frog_images/frog_7.png"))
        self.sprites.append(pygame.image.load("frog_images/frog_8.png"))
        self.sprites.append(pygame.image.load("frog_images/frog_9.png"))
        self.sprites.append(pygame.image.load("frog_images/frog_10.png"))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
        self.is_animating = False

    def animate(self):
        self.is_animating = True

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.25

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[int(self.current_sprite)]


pygame.init()

width, height = 400, 400
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
        if event.type == pygame.KEYDOWN:
            player.animate()

    screen.fill((0, 0, 0))

    player_group.draw(screen)
    player_group.update()

    pygame.display.update()
    clock.tick(60)
