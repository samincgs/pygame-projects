import pygame, sys, random


class Ship(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load("graphics/ship.png").convert_alpha()
        self.rect = self.image.get_rect(center=(screen_width / 2, screen_height / 2))
        self.mask = pygame.mask.from_surface(self.image)

        self.can_shoot = True
        self.shoot_time = None

        self.laser_sound = pygame.mixer.Sound("sounds/laser.ogg")
        self.laser_sound.set_volume(0.1)

    def input_position(self):
        mouse_pos = pygame.mouse.get_pos()
        self.rect.center = mouse_pos

    def laser_time(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time > 500:
                self.can_shoot = True

    def laser_shoot(self):
        mouse_input = pygame.mouse.get_pressed()[0]
        if mouse_input and self.can_shoot:
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()
            self.laser_sound.play()

            Laser(self.rect.midtop, laser_group)

    def meteor_collision(self):
        if pygame.sprite.spritecollide(
            self, meteor_group, True, pygame.sprite.collide_mask
        ):
            pygame.quit()
            sys.exit()

    def update(self):
        self.laser_time()
        self.laser_shoot()
        self.input_position()
        self.laser_shoot()
        self.meteor_collision()


class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load("graphics/laser.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=(pos))
        self.mask = pygame.mask.from_surface(self.image)

        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(0, -1)
        self.speed = 600

        self.explosion_sound = pygame.mixer.Sound("sounds/explosion.wav")
        self.explosion_sound.set_volume(0.1)

    def meteor_collision(self):
        if pygame.sprite.spritecollide(
            self, meteor_group, True, pygame.sprite.collide_mask
        ):
            self.explosion_sound.play()
            self.kill()

    def update(self):
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))
        if self.rect.bottom < 0:
            self.kill()

        self.meteor_collision()


class Meteor(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        meteor_surf = pygame.image.load("graphics/meteor.png").convert_alpha()
        meteor_size = pygame.math.Vector2(meteor_surf.get_size()) * random.uniform(
            0.5, 1.5
        )
        self.meteor_scaled = pygame.transform.scale(meteor_surf, meteor_size)

        self.image = self.meteor_scaled
        x = random.randint(10, screen_width - 10)
        y = random.randint(-150, 50)
        self.rect = self.image.get_rect(center=(x, y))
        self.mask = pygame.mask.from_surface(self.image)

        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(random.uniform(-0.5, 0.5), 1)
        self.speed = random.randint(400, 700)

        self.rotation = 0
        self.rotation_speed = random.randint(20, 50)

    def rotate(self):
        self.rotation += self.rotation_speed * dt
        rotate_surf = pygame.transform.rotozoom(self.meteor_scaled, self.rotation, 1)
        self.image = rotate_surf
        self.rect = self.image.get_rect(center=self.rect.center)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))
        if self.rect.top > screen_height:
            self.kill()

        self.rotate()


class Score:
    def __init__(self):
        self.font = pygame.font.Font("graphics/subatomic.ttf", 50)

    def display(self):
        score_text = f"Score: {pygame.time.get_ticks() // 1000}"
        score_surf = self.font.render(score_text, True, (255, 255, 255))
        score_rect = score_surf.get_rect(center=(screen_width / 2, 600))
        screen.blit(score_surf, score_rect)
        pygame.draw.rect(
            screen,
            (255, 255, 255),
            score_rect.inflate(40, 40),
            width=6,
            border_radius=10,
        )


pygame.init()

screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Asteroid Shooter")
clock = pygame.time.Clock()

# background
bg = pygame.image.load("graphics/background.png").convert()
bg_music = pygame.mixer.Sound("sounds/music.wav")
bg_music.set_volume(0.1)
bg_music.play(loops=-1)

meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 400)

# object calls
ship_group = pygame.sprite.GroupSingle()
laser_group = pygame.sprite.Group()
meteor_group = pygame.sprite.Group()

ship = Ship(ship_group)
score = Score()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == meteor_timer:
            Meteor(meteor_group)

    dt = clock.tick() / 1000

    screen.blit(bg, (0, 0))

    score.display()

    ship_group.draw(screen)
    laser_group.draw(screen)
    meteor_group.draw(screen)

    ship_group.update()
    laser_group.update()
    meteor_group.update()

    pygame.display.update()
