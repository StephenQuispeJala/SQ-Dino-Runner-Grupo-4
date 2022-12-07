from random import randint
import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS

class ObsctaclesManager:
    Y_POS_LARGE_CACTUS = 300
    Y_POS_SMALL_CACTUS = 325
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            if randint(0, 10) % 2 == 0:
                self.obstacles.append(Cactus(LARGE_CACTUS, self.Y_POS_LARGE_CACTUS))
            else:    
                self.obstacles.append(Cactus(SMALL_CACTUS, self.Y_POS_SMALL_CACTUS))
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)