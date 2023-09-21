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
