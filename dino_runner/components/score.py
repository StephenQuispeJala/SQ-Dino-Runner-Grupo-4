import pygame
from dino_runner.components.text import Text
from dino_runner.utils.constants import FONT_STYLE


class Score:
    def __init__(self):
        self.current_score = 0
        self.text = Text(30)

    def update(self, game):
        self.current_score += 1
        if self.current_score % 100 == 0:
            game.game_speed += 2

    def draw(self, screen):
        self.text.draw_text(f"Score {self.current_score}", 1000, 50, screen)
        