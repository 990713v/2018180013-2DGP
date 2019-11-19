from pico2d import *
import game_world

class Game_map:
    def __init__(self):
        # self.image = load_image('coin_map.png')
        self.image = load_image('original_map.png')
        self.image2 = load_image('black.png')
    
    def update(self):
        pass

    def draw(self):        
        self.image2.draw(324, 348)
        self.image.draw(324, 348)
