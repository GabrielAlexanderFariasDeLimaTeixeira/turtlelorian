import pygame

WIN_WID = 600
WIN_HGT = 600
SPEED = 20
GAME_SPEED = 10
SOIL_WID = 650
SOIL_HGT = 64


class ATSTurtle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = [pygame.image.load('images/A-Turtle1.png').convert_alpha(),
                       pygame.image.load('images/A-Turtle2.png').convert_alpha(),
                       pygame.image.load('images/A-Turtle3.png').convert_alpha(),
                       pygame.image.load('images/A-Turtle4.png').convert_alpha()]
        self.speed = SPEED
        self.current_image = 0
        self.image = pygame.image.load('images/A-Turtle1.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()


class CargoTurtle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = [pygame.image.load('images/cargo1.png').convert_alpha(),
                       pygame.image.load('images/cargo2.png').convert_alpha(),
                       pygame.image.load('images/cargo3.png').convert_alpha(),
                       pygame.image.load('images/cargo4.png').convert_alpha()]
        self.speed = SPEED*2
        self.current_image = 0
        self.image = pygame.image.load('images/cargo1.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()


class THunter(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__int__(self)

        self.images = [pygame.image.load('images/hunter1.png').convert_alpha(),
                       pygame.image.load('images/hunter2.png').convert_alpha(),
                       pygame.image.load('images/hunter3.png').convert_alpha(),
                       pygame.image.load('images/hunter4.png').convert_alpha()]
        self.speed = SPEED*4
        self.current_image = 0
        self.image = pygame.image.load('images/hunter1.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()


class Turtlelorian(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = [pygame.image.load('images/ttl1.png').convert_alpha(),
                       pygame.image.load('images/ttl2.png').convert_alpha(),
                       pygame.image.load('images/ttl3.png').convert_alpha(),
                       pygame.image.load('images/ttl4.png').convert_alpha()]
        self.speed = SPEED
        self.current_image = 0
        self.image = pygame.image.load('images/ttl1.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = WIN_WID / 3
        self.rect[1] = WIN_HGT / 2

    def update(self):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]

        if self.speed > 0.5:
            self.speed -= 1
        elif self.speed <= 0.5 and self.speed >= 0:
            self.speed -= 0.5
        elif self.speed >= -0.5 and self.speed <= 0:
            self.speed += 0.5
        else:
            self.speed += 1

        self.rect[1] += self.speed

    def jetpack_up(self):
        self.speed = -SPEED

    def jetpack_down(self):
        self.speed = SPEED


pygame.init()
screen = pygame.display.set_mode((WIN_WID, WIN_HGT))

BG = pygame.image.load('images/sand_place.png')
BG = pygame.transform.scale(BG, (WIN_WID, WIN_HGT))

ttl_gp = pygame.sprite.Group()
ttl = Turtlelorian()
ttl_gp.add(ttl)


class Ground(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('images/sand.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (SOIL_WID, SOIL_HGT))

        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = WIN_HGT - SOIL_HGT

    def update(self):
        self.rect[0] -= GAME_SPEED


def is_off_screen(sprite):
    return sprite.rect[0] < -(sprite.rect[2])


global ground_gp
ground_gp = pygame.sprite.Group()
for i in range(2):
    ground = Ground(SOIL_WID * i)
    ground_gp.add(ground)

global clock
clock = pygame.time.Clock()


def game_loop():
    run = True
    BGX = 0
    BGX2 = BG.get_width()

    while run:
        clock.tick(20)
        for event in pygame.event.get():
            press = pygame.key.get_pressed()
            if press[pygame.K_w] == 1:
                ttl.jetpack_up()
            if press[pygame.K_s] == 1:
                ttl.jetpack_down()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        BGX -= 1.4
        BGX2 -= 1.4

        if BGX < BG.get_width() * -1:
            BGX = BG.get_width()

        if BGX2 < BG.get_width() * -1:
            BGX2 = BG.get_width()

        # animation
        screen.blit(BG, (BGX, 0))
        screen.blit(BG, (BGX2, 0))

        if is_off_screen(ground_gp.sprites()[0]):
            ground_gp.remove(ground_gp.sprites()[0])
            new_ground = Ground(SOIL_WID - 20)
            ground_gp.add(new_ground)

        # ttl
        ttl_gp.update()
        ground_gp.update()
        ttl_gp.draw(screen)
        ground_gp.draw(screen)

        pygame.display.update()

        if(pygame.sprite.groupcollide(ttl_gp, ground_gp, False, False, pygame.sprite.collide_mask)):
            ttl.jetpack_up()
