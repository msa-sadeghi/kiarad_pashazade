import pygame
from old.player import Player

WIDTH = 1024
HEIGHT = 640

screen = pygame.display.set_mode((WIDTH, HEIGHT))
p = Player()


bg = pygame.image.load("BG.png")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
FPS = 60
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg, (0, 0))
    p.draw(screen)
    p.go()
    p.animation()
    pygame.display.update()
    CLOCK.tick(FPS)
