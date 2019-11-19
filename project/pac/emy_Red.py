from pico2d import *
import game_world

class Emy_Red:
    def __init__(self):
        self.x, self.y = 162, 180
        self.frame = 4
        self.image = load_image('red.png')

    def update(self):
        self.frame = (self.frame + 1) % 2


    def draw(self):
        self.image.clip_draw(self.frame * 58, 64, 58, 32, self.x, self.y)
