import pygame
from dino_runner.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH


class Text:
    half_screen_width = SCREEN_WIDTH // 2
    half_screen_height = SCREEN_HEIGHT // 2
    
    def __init__(self, size):
        self.font = pygame.font.Font(FONT_STYLE, size)

    def draw_text(self, message: str, x_pos, y_pos, screen: pygame.Surface):
        self.message = self.font.render(message, True, (0, 0, 0))
        self.message_rect = self.message.get_rect()    
        self.message_rect.center = (x_pos, y_pos)
        screen.blit(self.message, self.message_rect) 
           