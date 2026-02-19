import pygame
pygame.init()

WIDTH = 1000
HEIGHT = 640

screen = pygame.display.set_mode((WIDTH, HEIGHT))
rect =  pygame.Rect(10, 10, 50, 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                if rect.left > 0:
                    rect.x -= 5
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                if rect.right < WIDTH:
                    rect.x += 5
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                rect.y -= 5
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                rect.y += 5

    screen.fill("lightgreen")
    pygame.draw.ellipse(screen, "red",  rect)
    pygame.display.update()