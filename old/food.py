from pygame.sprite import Sprite
import pygame

class Food(Sprite):
    def __init__(self, image, x,y, points):
        super().__init__()
        self.image = pygame.transform.scale_by(image, 0.9)

        self.rect = self.image.get_rect(topleft=(x,y))
        self.points = points
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    

