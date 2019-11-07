from pico2d import *

class Game_map:
    def __init__(self):
        self.image = load_image('coin_map.png')
        self.image2 = load_image('black.png')

    def update(self):
        pass

    def draw(self):
        
        self.image2.draw(162, 174)
        self.image.draw(162, 174)
