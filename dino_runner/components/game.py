import pygame
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacles_manager import ObsctaclesManager
from dino_runner.components.player_hearts.player_heart_manager import PlayerHeartManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.score import Score
from dino_runner.components.text import Text
from dino_runner.utils.constants import BG, DINO_RESTART, DINO_START, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS

INITIAL_GAME_SPEED = 20

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = INITIAL_GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.player = Dinosaur()
        self.obstacle_manager = ObsctaclesManager()
        self.player_heart_manager = PlayerHeartManager()
        self.power_up_manager = PowerUpManager()
        self.score = Score()
        self.max_score_txt = Text(20)
        self.text = Text(30)
        self.death_count = 0
        self.max_score = 0
        self.executing = False

    def execute(self):
        self.executing = True        
        while self.executing:
            if not self.playing:
                self.show_menu()
              
        pygame.quit()    

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.initialize_game()
        while self.playing:
            self.events()
            self.update()
            self.draw()
        
    def initialize_game(self):
        self.obstacle_manager.reset_obstacles()
        self.max_score = self.score.current_score if self.score.current_score > self.max_score else self.max_score
        self.score.current_score = 0
        self.game_speed = INITIAL_GAME_SPEED
        self.player_heart_manager.reset_heart_count()
        self.power_up_manager.reset_power_ups()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.score.update(self)
        self.power_up_manager.update(self.score.current_score, self.game_speed, self.player)
        

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
        self.max_score_txt.draw_text(f"Last Max Score {self.max_score}", SCREEN_WIDTH - 150, SCREEN_HEIGHT - 20, self.screen)
        self.power_up_manager.draw(self.screen)
        self.player_heart_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
            
        self.x_pos_bg -= self.game_speed

    def show_menu(self):
        self.screen.fill((255, 255, 255)) # Poner color al fondo
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2
        if not self.death_count:
            self.text.draw_text("Press Any Key To Start", half_screen_width, half_screen_height, self.screen) # Mostrar mensaje de inicio
            self.screen.blit(DINO_START, (half_screen_width - 40, half_screen_height - 140)) # Mostrar imagen como icono     
        else:
            self.text.draw_text("Press Any Key To Restart", half_screen_width, half_screen_height, self.screen)
            self.text.draw_text(f"Score {self.score.current_score}      Deaths {self.death_count}", half_screen_width, half_screen_height + 50, self.screen)
            self.max_score_txt.draw_text(f"Last Max Score {self.max_score}", half_screen_width, half_screen_height+100, self.screen)
            self.screen.blit(DINO_RESTART, (half_screen_width - 40, half_screen_height - 140)) # Mostrar imagen como icono     
            
    # Actualizar pantalla
        pygame.display.flip()
    # Manejar eventos    
        self.handle_menu_events()
   
    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False
            elif event.type == pygame.KEYDOWN:
                self.run()