import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        self.image = pygame.Surface((50, 50))
        self.image.fill("red")
        self.rect = self.image.get_rect(center=(pos))

    def player_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            print("UP")
        if keys[pygame.K_DOWN]:
            print("DOWN")
        if keys[pygame.K_RIGHT]:
            print("RIGHT")
        if keys[pygame.K_LEFT]:
            print("LEFT")

    def update(self):
        self.player_input()
