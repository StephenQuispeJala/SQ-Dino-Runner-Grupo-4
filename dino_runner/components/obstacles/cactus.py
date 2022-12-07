from random import randint
from pygame import Surface
from dino_runner.components.obstacles.obstacle import Obstacle

class Cactus(Obstacle):
    
    def __init__(self, images: list[Surface], y_pos):
        super().__init__(images, randint(0, 2))
        self.rect.y = y_pos