from constants import *
import pygame

class Cell():
    def __init__(self, x, y):
        self.size = WIDTH / AMOUNT_WIDTH
        self.rect_black = pygame.Rect(x, y, self.size, self.size)
        self.rect_white = pygame.Rect(x + 1, y + 1, self.size - 2, self.size - 2)
        self.is_fill = False


    def draw(self, surface):
        if self.is_fill:
            pygame.draw.rect(surface, WHITE, self.rect_white)
        else:
            pygame.draw.rect(surface, WHITE, self.rect_black, 1)
