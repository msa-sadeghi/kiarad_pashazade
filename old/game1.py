import pygame
import random
pygame.init()

window = pygame.display.set_mode((640, 480))
red = 0
green = 0
blue = 0

lion_image = pygame.image.load("lion.png")
lion_image = pygame.transform.scale_by(lion_image, 0.5)
lion_rect = lion_image.get_rect(topleft=(400, 50))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            red = random.randint(0,255)
            green = random.randint(0,255)
            blue = random.randint(0,255)

    # window.fill((255, 255, 0))
    # window.fill("yellow")
    window.fill((red, green, blue))
    window.blit(lion_image, lion_rect)
    pygame.display.update()