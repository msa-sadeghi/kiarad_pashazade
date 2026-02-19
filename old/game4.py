import pygame
from old.character import Character


WIDTH = 1000
HEIGHT = 640

screen = pygame.display.set_mode((WIDTH, HEIGHT))
player1_image = pygame.image.load("lion.png")
player1 = Character(player1_image, 50, 100, 0.5)

player2_image = pygame.image.load("tiger.png")
player2= Character(player2_image, 200, 400, 1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("pink")
    player1.draw(screen)
    player1.move()
    player2.draw(screen)
    player2.move()
    pygame.display.update()