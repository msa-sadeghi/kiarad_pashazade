import pygame
pygame.init()
WIDTH = 800
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 0,0)
GREEN = (0, 255,0)
BLUE = (0, 0,255)
color = RED
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_r:
                color = RED
            elif event.key == pygame.K_g:
                color = GREEN
            elif event.key == pygame.K_b:
                color = BLUE

    screen.fill(color)
    pygame.display.update()
                
