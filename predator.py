import pygame

class Predator:
    def __init__(self, position_x, position_y, size):
        self.color = (0, 0, 100)
        self.rect = pygame.Rect(position_x, position_y, size, size)
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)