from pico2d import *
import game_world
##

class Coin:
    def __init__(self):
        self.image = load_image('coin.png')
        ##ㄹ ㅣ소스 수정할것

    def update(self):
        pass


    def draw(self):
        self.image.draw(162, 174)
