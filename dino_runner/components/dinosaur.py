import pygame
from pygame.sprite import Sprite
from dino_runner.components.text import Text
from dino_runner.utils.constants import DEFAULT_TYPE, DUCKING, DUCKING_HAMMER, DUCKING_SHIELD, HAMMER_TYPE, JUMPING, JUMPING_HAMMER, JUMPING_SHIELD, RUNNING, RUNNING_HAMMER, RUNNING_SHIELD, SHIELD_TYPE

DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER} 
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER} 
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER} 

class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    JUMP_VELOCITY = 8.5
    DUCK_Y_POS = Y_POS + 32

    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0] 
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.jump_velocity = self.JUMP_VELOCITY
        self.step_index = 0
        self.running = True
        self.jumping = False
        self.ducking = False

        self.hammer = False
        self.shield = False
        self.power_time_up = 0

        self.has_power_up = False
        self.show_text = False

        self.power_up_text = Text(18)

    def update(self, user_input):        
        if user_input[pygame.K_UP] and not self.jumping:
            self.jumping = True
            self.running = False
            self.ducking = False
        elif user_input[pygame.K_DOWN] and not self.jumping:
            self.ducking = True
            self.running = False
            self.jumping = False
        elif not self.jumping:
            self.running = True
            self.jumping = False
            self.ducking = False    

        if self.running:
            self.run()    
        elif self.jumping:
            self.jump()
        elif self.ducking:
            self.duck()

        if self.step_index >= 10:
            self.step_index = 0

    def run(self):
        self.image = RUN_IMG[self.type][0] if self.step_index < 5 else RUN_IMG[self.type][1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = JUMP_IMG[self.type]
        self.dino_rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.8
        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.dino_rect.y = self.Y_POS
            self.jumping = False
            self.jump_velocity = self.JUMP_VELOCITY  

    def duck(self):
        self.image = DUCK_IMG[self.type][0] if self.step_index < 5 else DUCK_IMG[self.type][1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.DUCK_Y_POS
        self.step_index += 1

    def draw(self, screen):
        self.check_power_up(screen)
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def check_power_up(self, screen: Sprite):
        if self.shield or self.hammer:
            time_to_show = round((self.power_time_up - pygame.time.get_ticks())/ 1000, 2)
            if time_to_show >= 0 and self.show_text:
                pos_x_center = 500
                pos_y_center = 40 
                self.power_up_text.draw_text(f"Shield enabe for ", pos_x_center, pos_y_center, screen) 
                self.power_up_text.draw_text(f"{time_to_show}", pos_x_center + 150, pos_y_center, screen) 
            else:
                self.shield = False
                self.hammer = False
                self.type = DEFAULT_TYPE 

        

