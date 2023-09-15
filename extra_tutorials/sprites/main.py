import pygame, sys, random


class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        # self.gunshot = pygame.mixer.Sound()

    def shoot(self):
        pygame.sprite.spritecollide(crosshair, target_group, True)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)


pygame.init()

screen_width, screen_height = 1200, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Aim Trainer")
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

background = pygame.transform.scale(
    pygame.image.load("images/bg_blue.png"), (screen_width, screen_height)
).convert()

crosshair = Crosshair("images/crosshair.png")

crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

target_group = pygame.sprite.Group()

for target in range(12):
    new_target = Target(
        "images/target_red2.png",
        random.randrange(0, screen_width),
        random.randrange(0, screen_height),
    )
    target_group.add(new_target)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            crosshair.shoot()

    screen.blit(background, (0, 0))

    target_group.draw(screen)
    crosshair_group.draw(screen)

    crosshair_group.update()

    pygame.display.update()
    clock.tick(60)
