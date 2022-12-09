from random import randint
import pygame
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.shield import Shield

class PowerUpManager:
    POWER_UPS = {
        1 : Shield(),
        2 : Hammer() 
    }

    def __init__(self):
        self.power_ups = []
        self.when_appears = 0
        self.selection = 0
        

    def generate_power_up(self, current_score):
        if len(self.power_ups) == 0:
            if self.when_appears == current_score:
                self.when_appears = randint(self.when_appears + 200, self.when_appears + 300)
                self.selection = randint(1, 2)
                self.power_ups.append(self.POWER_UPS[self.selection])

    def update(self, current_score, game_speed, player):
        self.generate_power_up(current_score)            
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                if self.selection == 1:
                    player.shield = True
                elif self.selection == 2:    
                    player.hammer = True
                player.show_text = True
                player.type = power_up.type
                time_random = randint(5, 7)
                player.power_time_up = power_up.start_time + (time_random * 1000)
                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)            

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = randint(200, 300)
        self.selection = 0