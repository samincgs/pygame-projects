import pygame
from os import walk
from random import choice


class Car(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)

        for _, _, img_list in walk("graphics/cars"):
            car_color = choice(img_list)

        self.image = pygame.image.load(f"graphics/cars/{car_color}")
        self.rect = self.image.get_rect(center=pos)

        self.pos = pygame.math.Vector2(self.rect.center)

        if self.pos[0] < 200:
            self.direction = pygame.math.Vector2(1, 0)
        else:
            self.direction = pygame.math.Vector2(-1, 0)
            self.image = pygame.transform.flip(self.image, True, False)

        self.speed = 300

    def move(self, dt):
        self.pos += self.direction * self.speed * dt
        self.rect.center = (round(self.pos.x), round(self.pos.y))

    def update(self, dt):
        self.move(dt)

        if not -200 < self.rect.x < 3400:
            self.kill()
