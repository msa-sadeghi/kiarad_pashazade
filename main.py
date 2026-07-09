import pygame
import os

WIDTH = 1024
HEIGHT = 640

screen = pygame.display.set_mode((WIDTH, HEIGHT))

ASSETS_PATH = "robot"


def load_frames(folder_name):
    path = os.path.join(ASSETS_PATH, folder_name)
    frames = []
    files = sorted(os.listdir(path))
    for f in files:
        img = pygame.image.load()

load_frames("Dead")


bg_image = pygame.image.load("BG.png")
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
running = True

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # screen.fill("lightgreen")
    screen.blit(bg_image, (0, 0))
    pygame.display.update()
