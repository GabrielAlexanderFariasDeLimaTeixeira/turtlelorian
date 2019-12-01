import pygame
import random

IMG_DIR = "images/"
pygame.init()

global win
x = 50
y = 50
width = 40
height = 60
vel = 5

pygame.display.set_caption("Turtlelorian")
win = pygame.display.set_mode((576, 288))
bg = pygame.image.load(IMG_DIR+"sand_place.png").convert_alpha()

pygame.draw.rect(win, (54, 182, 112), (x, y, width, height))
clock = pygame.time.Clock()


def screen_redraw():
    win.blit(bg, (0, 0))
    pygame.display.update()


intro = True

while intro:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            intro = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 576 - vel - width:
        x += vel
    if keys[pygame.K_UP] and y > vel:
        y -= vel
    if keys[pygame.K_DOWN] and y < 288 - vel - height:
        y += vel

    pygame.draw.rect(win, (54, 182, 112), (x, y, width, height))
    screen_redraw()


pygame.quit()
