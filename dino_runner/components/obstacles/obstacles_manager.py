from random import randint
import pygame
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS

class ObsctaclesManager:
    Y_POS_LARGE_CACTUS = 300
    Y_POS_SMALL_CACTUS = 325
    Y_POS_BIRD = 245
    
    def __init__(self):
        self.obstacles = []
        self.number = 0

    def update(self, game):
        if len(self.obstacles) == 0:
            self.number = randint(1, 3)
            if self.number == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS, self.Y_POS_LARGE_CACTUS))
            elif self.number == 2:    
                self.obstacles.append(Cactus(SMALL_CACTUS, self.Y_POS_SMALL_CACTUS))
            elif self.number == 3:
                self.obstacles.append(Bird(self.Y_POS_BIRD))
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if not game.player.shield:
                if not game.player.hammer:
                    if game.player.dino_rect.colliderect(obstacle.rect):
                        game.player_heart_manager.reduce_heart_count()
                        if game.player_heart_manager.heart_count > 0:
                            self.obstacles.pop()
                        else:
                            game.playing = False
                            game.death_count += 1
                else:            
                    if game.player.dino_rect.colliderect(obstacle.rect):
                        obstacle.rect.y += randint(-100, 100)    
                        
                        

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):        
        self.obstacles = []