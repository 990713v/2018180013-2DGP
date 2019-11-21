from pico2d import *
import game_world
import game_framework
import random


class Coin:
    image = None
    
    def __init__(self):
        self.image = load_image('small_coin.png')
        #self.image2 = load_image('big_coin.png')

        self.x, self.y = random.randint(200, 400), random.randint(200, 400)

    def get_bb(self):
        return self.x - 5, self.y - 5, self.x + 5, self.y + 5

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x = self.x

    
