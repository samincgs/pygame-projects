import pygame, sys


class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        # self.gunshot = pygame.mixer.Sound()

    # def shoot(self):

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


pygame.init()

screen_width, screen_height = 1120, 680
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


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))

    crosshair_group.draw(screen)
    crosshair_group.update()

    pygame.display.update()
    clock.tick(60)
