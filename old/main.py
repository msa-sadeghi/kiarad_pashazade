import pygame
from player import Player
from food import Food
from elien import Alien
import random
pygame.init()
WIDTH = 1000
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
CLOCK = pygame.time.Clock()
bg_image = pygame.image.load("BG.png")
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
player_image = pygame.image.load("player.png")
my_player = Player(player_image, 400, 400)

egg_image = pygame.image.load("egg.png")

egg = Food(egg_image, random.randint(50, 900), 0, 10)

alian1_image = pygame.image.load("alian1.png")
alian2_image = pygame.image.load("alian2.png")

alian1 = Alien(alian1_image, 40, 0, 3, 1)
alian2 = Alien(alian2_image, 490, 0, 4, 2)


FPS = 60
CLOCK = pygame.time.Clock()
score = 0
running = True
while running == True:
    CLOCK.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    CLOCK.tick(FPS)
    egg.rect.y += 5
    if egg.rect.bottom >= HEIGHT:
        x = random.randint(50, 900)
        egg.rect.x = x
        egg.rect.y = 0

    if my_player.rect.colliderect(egg.rect):
        score += 1
        x = random.randint(50, 900)
        egg.rect.x = x
        egg.rect.y = 0
    if my_player.rect.colliderect(alian1.rect):
        score -= 1
        x = random.randint(50, 900)
        alian1.rect.x = x
        alian1.rect.y = 0
    if my_player.rect.colliderect(alian2.rect):
        score -= 1
        x = random.randint(50, 900)
        alian2.rect.x = x
        alian2.rect.y = 0

    screen.blit(bg_image, (0,0))
    my_player.draw(screen)
    my_player.move()
    alian1.draw(screen)
    alian2.draw(screen)
    alian1.move()
    alian2.move()
    egg.draw(screen)
    pygame.display.update()