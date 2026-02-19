import pygame


WIDTH = 1024
HEIGHT = 640


PAGE = pygame.display.set_mode((WIDTH,HEIGHT))
running = True
while running == True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
        

    PAGE.fill("pink")
    pygame.display.update()