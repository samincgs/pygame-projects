import pygame
from os import walk


class Player(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)

        self.import_assets()
        self.frame_index = 0
        self.status = "down"
        # self.image = self.animation[self.frame_index]
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=(pos))

        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 200

    def import_assets(self):
        # path = "graphics/player/right/"
        # self.animation = [pygame.image.load(f"{path}{frame}.png") for frame in range(4)]

        self.animations = {}
        # better import
        for index, folder in enumerate(walk("graphics/player")):
            if index == 0:
                for directions in sorted(folder[1]):
                    self.animations[directions] = []
            else:
                for images in sorted(folder[2]):
                    path = f"{folder[0]}/{images}"
                    surf = pygame.image.load(path).convert_alpha()
                    key = folder[0].split("/")[-1]
                    self.animations[key].append(surf)

                # self.animations[key].append(surf)
        print(self.animations)

    def move(self, dt):
        self.pos += self.direction * self.speed * dt
        self.rect.center = (round(self.pos.x), round(self.pos.y))

    def animate(self, dt):
        current_animation = self.animations[self.status]

        self.frame_index += 10 * dt
        if self.frame_index >= len(current_animation):
            self.frame_index = 0
        self.image = current_animation[int(self.frame_index)]

        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        print(current_animation)

    def input(self):
        keys = pygame.key.get_pressed()

        # up and down
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = "up"
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = "down"
        else:
            self.direction.y = 0

        # right and left
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = "right"
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = "left"
        else:
            self.direction.x = 0

    def update(self, dt):
        self.input()
        self.move(dt)
        self.animate(dt)
