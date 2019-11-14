from pico2d import *
import game_world

class Emy_Orange:
    def __init__(self):
        self.x, self.y = 210, 180
        self.frame = 4
        self.image = load_image('orange.png')

    def update(self):
        self.frame = (self.frame + 1) % 4


    def draw(self):
        self.image.clip_draw(self.frame * 29, 32, 29, 16, self.x, self.y)
