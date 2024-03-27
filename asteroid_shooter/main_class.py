import pygame, sys
from random import randint, uniform


class Ship(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        self.image = pygame.image.load("graphics/ship.png").convert_alpha()
        self.rect = self.image.get_rect(center=(WIDTH / 2, HEIGHT / 2))

        self.canshoot = True
        self.shoot_time = None

        self.laser_sound = pygame.mixer.Sound("./sounds/laser.ogg")

    def input(self):
        mouse_pos = pygame.mouse.get_pos()
        self.rect.center = mouse_pos

    def laser_shoot(self):
        mouse_click = pygame.mouse.get_pressed()

        if mouse_click[0] and self.canshoot:
            Laser(self.rect.midtop, laser_sprites)
            self.shoot_time = pygame.time.get_ticks()
            self.canshoot = False
            self.laser_sound.play()

    def laser_timer(self):
        if not self.canshoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time > 500:
                self.canshoot = True

    def meteor_collision(self):
        if pygame.sprite.spritecollide(self, meteor_sprites, False):
            pygame.quit()
            sys.exit()
            pass

    def update(self):
        self.laser_timer()
        self.input()
        self.laser_shoot()
        self.meteor_collision()


class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.image.load("graphics/laser.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)

        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(0, -1)
        self.speed = 600

        self.explosion_sound = pygame.mixer.Sound("./sounds/explosion.wav")

    def meteor_collision(self):
        if pygame.sprite.spritecollide(self, meteor_sprites, True):
            self.kill()
            self.explosion_sound.play()

    def update(self):
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))

        if self.rect.bottom <= 0:
            self.kill()

        self.meteor_collision()


class Meteor(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        meteor_surf = pygame.image.load("graphics/meteor.png").convert_alpha()
        meteor_size = pygame.math.Vector2(meteor_surf.get_size()) * uniform(0.5, 1.5)
        self.scaled_surf = pygame.transform.scale(meteor_surf, meteor_size)
        self.image = self.scaled_surf
        self.rect = self.image.get_rect(topleft=pos)

        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(uniform(-0.5, 0.5), 1)
        self.speed = randint(400, 600)

        # rotation logic
        self.rotation = 0
        self.rotation_speed = randint(20, 50)

    def rotate(self):
        self.rotation += self.rotation_speed * dt
        rotated_surf = pygame.transform.rotozoom(self.scaled_surf, self.rotation, 1)
        self.image = rotated_surf
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))
        self.rotate()

        if self.rect.bottom > HEIGHT:
            self.kill()


class Score:
    def __init__(self):
        self.font = pygame.font.Font("graphics/subatomic.ttf", 50)

    def display(self):
        score_text = f"Score: {pygame.time.get_ticks() // 1000}"
        text_surf = self.font.render(score_text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(midbottom=(WIDTH / 2, HEIGHT - 80))
        screen.blit(text_surf, text_rect)
        pygame.draw.rect(
            screen, (255, 255, 255), text_rect.inflate(30, 30), width=8, border_radius=5
        )


pygame.init()
pygame.display.set_caption("Asteroid Shooter")

WIDTH, HEIGHT = 1280, 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bg = pygame.image.load("graphics/background.png").convert()

ship_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()

ship = Ship(ship_sprites)

score = Score()

bg_music = pygame.mixer.Sound("./sounds/music.wav")
bg_music.play(loops=-1)


meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 400)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == meteor_timer:
            meteor_y_pos = randint(-150, -50)
            meteor_x_pos = randint(-100, WIDTH + 100)
            Meteor((meteor_x_pos, meteor_y_pos), meteor_sprites)

    dt = clock.tick() / 1000

    screen.blit(bg, (0, 0))

    ship_sprites.update()
    meteor_sprites.update()
    laser_sprites.update()

    score.display()

    ship_sprites.draw(screen)
    laser_sprites.draw(screen)
    meteor_sprites.draw(screen)

    pygame.display.update()
