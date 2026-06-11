import pygame
from pygame.sprite import Sprite
import os


class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.animations = ("Dead", "Idle", "Jump", "Run", "Shoot", "Slide")
        self.all_images = {}

        for anim in self.animations:
            images = []
            n = len(os.listdir(f"robot/{anim}"))
            for i in range(1, n + 1):
                img = pygame.image.load(f"robot/{anim}/{anim} ({i}).png")
                img = pygame.transform.scale_by(img, 0.3)
                images.append(img)
            self.all_images[anim] = images

        self.image = self.all_images["Idle"][0]
        self.frame_index = 0
        self.rect = self.image.get_rect(topleft=(100, 400))
        self.last_animation_time = pygame.time.get_ticks()
        self.current_animation = "Idle"
        self.direction = 1

    def animation(self):
        if pygame.time.get_ticks() - self.last_animation_time >= 200:
            self.frame_index += 1
            if self.frame_index >= len(self.all_images[self.current_animation]):
                self.frame_index = 0
            self.last_animation_time = pygame.time.get_ticks()

    def draw(self, screen):
        img = self.all_images[self.current_animation][self.frame_index]
        if self.direction == -1:
            img = pygame.transform.flip(img, True, False)
        screen.blit(img, self.rect)

    def go(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.change_animation("Run")
            self.rect.x -= 300 * dt
            self.direction = -1
        if keys[pygame.K_RIGHT]:
            self.change_animation("Run")
            self.rect.x += 300 * dt
            self.direction = 1

        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.change_animation("Idle")

    def change_animation(self, new_animation):
        if new_animation != self.current_animation:
            self.current_animation = new_animation
            self.frame_index = 0
