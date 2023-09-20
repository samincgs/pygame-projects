import pygame, sys
from os import walk


class Player(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        self.import_assets()

        self.frame_index = 0
        self.status = "right"

        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=(pos))

        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2()
        self.speed = 200

    def animate(self, dt):
        current_animation = self.animations[self.status]

        if self.direction.magnitude() != 0:
            self.frame_index += 10 * dt
            if self.frame_index >= len(current_animation):
                self.frame_index = 0
        else:
            self.frame_index = 0

        self.image = current_animation[int(self.frame_index)]

    def move(self, dt):
        self.pos += self.direction * self.speed * dt
        self.rect.center = (round(self.pos.x), round(self.pos.y))

        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

    def import_assets(self):
        images_folder = walk("player")
        self.animations = {}
        for index, folder in enumerate(images_folder):
            if index == 0:
                for directions in sorted(folder[1]):
                    self.animations[directions] = []
            else:
                direction = folder[0].split("/")[1]
                for num in sorted(folder[2]):
                    surf = pygame.image.load(f"player/{direction}/{num}")
                    self.animations[direction].append(surf)
                print(self.animations)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = "up"
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = "down"
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = "left"
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = "right"
        else:
            self.direction.x = 0

    def update(self, dt):
        self.input()
        self.move(dt)
        self.animate(dt)


pygame.init()

width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Player Movements")
clock = pygame.time.Clock()

player_sprites = pygame.sprite.Group()

player = Player(player_sprites, (500, 200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("Black")

    dt = clock.tick() / 1000

    player_sprites.update(dt)

    player_sprites.draw(screen)

    pygame.display.update()
