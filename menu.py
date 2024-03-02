from constants import *
import pygame

class Menu():
    def __init__(self, width_frame):
        self.border = pygame.Rect(WIDTH, 0, WIDTH_MENU, WIDTH * 2)
        self.width_frame = width_frame
        self.score_border = pygame.Rect(WIDTH + WIDTH_MENU * 0.1, WIDTH * 0.1, WIDTH_MENU * 0.8, WIDTH * 0.1)
        self.level_border = pygame.Rect(WIDTH + WIDTH_MENU * 0.1, WIDTH * 0.3, WIDTH_MENU * 0.8, WIDTH * 0.1)
        self.font_style = pygame.font.SysFont('Arial', int(WIDTH * 0.08))

    def draw(self, surface, score, level):
        pygame.draw.rect(surface, WHITE, self.border, self.width_frame)
        pygame.draw.rect(surface, WHITE, self.score_border, self.width_frame)
        pygame.draw.rect(surface, WHITE, self.level_border, self.width_frame)
        score_text = self.font_style.render('SCORE', True, WHITE)
        score_image = self.font_style.render(str(score), True, WHITE)
        level_text = self.font_style.render('LEVEL', True, WHITE)
        level_image = self.font_style.render(str(level), True, WHITE)
        surface.blit(score_image, (self.score_border.x + 5, self.score_border.y + WIDTH * 0.005))
        surface.blit(score_text, (self.score_border.x + 5, self.border.y + WIDTH * 0.005))
        surface.blit(level_image, (self.level_border.x + 5, self.level_border.y + WIDTH * 0.005))
        surface.blit(level_text, (self.level_border.x + 5, self.score_border.bottom + WIDTH * 0.005))