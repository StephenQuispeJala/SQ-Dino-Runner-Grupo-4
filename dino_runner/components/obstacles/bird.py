from pygame import Surface
from dino_runner.components.obstacles.obstacle import Obstacle
from pygame.sprite import Sprite
from dino_runner.utils.constants import BIRD, SCREEN_WIDTH


class Bird(Sprite):
    def __init__(self, y_pos):
        self.images = BIRD[0]
        self.rect = self.images.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = y_pos
        self.step_index = 0

    def update(self, game_speed, obstacles: list):
        self.fly()
        if self.step_index >= 10:
            self.step_index = 0

        self.rect.x -= game_speed
        if self.rect.x <= -self.rect.width:
            obstacles.pop()    
 
    def fly(self):
        self.images = BIRD[0] if self.step_index < 5 else BIRD[1] 
        self.step_index += 1

    def draw(self, screen: Surface):
        screen.blit(self.images, (self.rect.x, self.rect.y))    