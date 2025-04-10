import pygame

class Prey:
    def __init__(self, x, y, size):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = (252, 200, 20)
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)