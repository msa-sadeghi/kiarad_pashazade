<<<<<<< HEAD
import pygame

class Character:
    def __init__(self, image, x,y, scale):
        self.image = pygame.transform.scale_by(image, scale)
        self.rect = self.image.get_rect(topleft=(x,y))
        self.speed = 5
        self.lives = 3
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
=======
import pygame

class Character:
    def __init__(self, image, x,y, scale):
        self.image = pygame.transform.scale_by(image, scale)
        self.rect = self.image.get_rect(topleft=(x,y))
        self.speed = 5
        self.lives = 3
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
>>>>>>> ac17a49582ab529e006253024bc5a2c43a965a07
            self.rect.x += self.speed