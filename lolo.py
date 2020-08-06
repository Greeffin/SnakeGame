import random
import sys

import pygame

pygame.init()
pygame.display.set_caption("Snake")
mainClock = pygame.time.Clock()
blocks = []
row = 20
column = 20
screen = pygame.display.set_mode((row * 25, column * 25))
imgfrt = pygame.transform.scale(pygame.image.load("fruit.png"), (25, 25))
imghad = pygame.transform.scale(pygame.image.load("snake__head.png"), (25, 25))
imgbod = pygame.transform.scale(pygame.image.load("snake__body.png"), (25, 25))
for i in range(row):
    for j in range(column):
        blocks.append((i, j))
snakes_block = [(2, 10), (1, 10)]
up = down = left = skip = False
right = True
for i in snakes_block:
    blocks.remove(i)
fruit = random.choice(blocks)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and left == False:
                right = True
                up = False
                down = False
            elif event.key == pygame.K_LEFT and right == False:
                left = True
                up = False
                down = False
            elif event.key == pygame.K_DOWN and up == False:
                down = True
                right = False
                left = False
            elif event.key == pygame.K_UP and down == False:
                up = True
                right = False
                left = False

    if up:
        next = (snakes_block[0][0], snakes_block[0][1] - 1)
        imghadd = pygame.transform.rotate(imghad, 180)
    elif down:
        next = (snakes_block[0][0], snakes_block[0][1] + 1)
        imghadd = pygame.transform.rotate(imghad, 360)
    elif left:
        next = (snakes_block[0][0] - 1, snakes_block[0][1])
        imghadd = pygame.transform.rotate(imghad, 270)
    elif right:
        next = (snakes_block[0][0] + 1, snakes_block[0][1])
        imghadd = pygame.transform.rotate(imghad, 90)

    if snakes_block[0] == fruit:
        fruit = random.choice(blocks)
        skip = True
    screen.fill((0, 0, 0))
    screen.blit(imgfrt, (fruit[0] * 25, fruit[1] * 25))
    for i in snakes_block:
        # pygame.draw.rect(screen, (0,255,0), (i[0]*25,i[1]*25,25,25))
        screen.blit(imgbod, (i[0] * 25, i[1] * 25))

    screen.blit(imghadd, (snakes_block[0][0] * 25, snakes_block[0][1] * 25))

    # noinspection PyUnboundLocalVariable
    snakes_block.insert(0, next)
    if not skip:
        blank = snakes_block.pop()
        blocks.append(blank)
    skip = False

    pygame.display.update()
    if next not in blocks:
        break
    blocks.remove(next)
    pygame.time.delay(500)
    mainClock.tick(40)
