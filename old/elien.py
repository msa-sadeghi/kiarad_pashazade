<<<<<<< HEAD
from pygame.sprite import Sprite
import pygame
import random
class Alien(Sprite):
    def __init__(self, image, x,y, speed, damage):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft = (x,y))
        self.speed = speed
        self.damage = damage

    def move(self):
        self.rect.y += self.speed
        if self.rect.bottom >= 640:
            self.rect.x = random.randint(50, 900)
            self.rect.y= 0

    def draw(self, screen):
=======
from pygame.sprite import Sprite
import pygame
import random
class Alien(Sprite):
    def __init__(self, image, x,y, speed, damage):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft = (x,y))
        self.speed = speed
        self.damage = damage

    def move(self):
        self.rect.y += self.speed
        if self.rect.bottom >= 640:
            self.rect.x = random.randint(50, 900)
            self.rect.y= 0

    def draw(self, screen):
>>>>>>> ac17a49582ab529e006253024bc5a2c43a965a07
        screen.blit(self.image, self.rect)