import pygame
import sys

lvl = []

try:
    f = open("level1.txt")
    lvl = f.read().split('\n')
    f.close()
except:
    sys.exit()
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
start = pygame.image.load("fon.jpg")
start = pygame.transform.scale(start, size)
flag = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            flag = 1
            break
        screen.fill((0, 0, 0))
    screen.blit(start, (0, 0))
    pygame.display.flip()
    if flag:
        break

FPS = 60
clock = pygame.time.Clock()
grass = pygame.image.load('grass.png').convert_alpha()
box = pygame.image.load('box.png').convert_alpha()
mario = pygame.image.load('mario.png').convert_alpha()
x = 4
y = 4
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if y != 0 and lvl[y - 1][x] != '#':
                    y -= 1
            if event.key == pygame.K_s:
                if y != len(lvl) - 1 and lvl[y + 1][x] != '#':
                    y += 1
            if event.key == pygame.K_a:
                if x != 0 and lvl[y][x - 1] != '#':
                    x -= 1
            if event.key == pygame.K_d:
                if x != len(lvl[0]) - 1 and lvl[y][x + 1] != '#':
                    x += 1
    screen.fill((0, 0, 0))
    for i in range(len(lvl)):
        for j in range(len(lvl[i])):
            if lvl[i][j] == '.':
                screen.blit(grass, (j * 50, i * 50))
            else:
                screen.blit(box, (j * 50, i * 50))
    screen.blit(mario, (x * 50 + 13, y * 50 + 5))
    flag = 0
    clock.tick(FPS)
    pygame.time.delay(1)
    pygame.display.flip()