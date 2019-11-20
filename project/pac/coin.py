from pico2d import *
import game_world
##

class Coin:
    def __init__(self):
        self.image = load_image('small_coin.png')
        #self.image2 = load_image('big_coin.png')        

    def update(self):
        pass


    def draw(self):
        for i in range(1, 10):
            for j in range (1, 10):
                self.image.draw(140 + 22*i, 140 + 22 * j)
        #self.image2.draw(184, 174)
