import random
import json
import os

from pico2d import *
import game_framework
import title_state

from player import Player

name = "MainState"
os.chdir('resourse')

game_map = None
player = None

# < 적 오브젝트 >
emy_Red = None
emy_Blue = None
emy_Pink = None
emy_Orange = None

class Game_map:
    def __init__(self):
        self.image = load_image('coin_map.png')
        self.image2 = load_image('black.png')

    def draw(self):
        
        self.image2.draw(162, 174)
        self.image.draw(162, 174)


# < 적 오브젝트>
class Emy_Red:
    def __init__(self):
        self.x, self.y = 162, 180
        self.frame = 4
        self.image = load_image('red.png')

    def update(self):
        self.frame = (self.frame + 1) % 4


    def draw(self):
        self.image.clip_draw(self.frame * 29, 32, 29, 16, self.x, self.y)


class Emy_Blue:
    def __init__(self):
        self.x, self.y = 191, 180
        self.frame = 4
        self.image = load_image('blue.png')

    def update(self):
        self.frame = (self.frame + 1) % 4


    def draw(self):
        self.image.clip_draw(self.frame * 29, 32, 29, 16, self.x, self.y)


class Emy_Pink:
    def __init__(self):
        self.x, self.y = 210, 180
        self.frame = 4
        self.image = load_image('pink.png')

    def update(self):
        self.frame = (self.frame + 1) % 4


    def draw(self):
        self.image.clip_draw(self.frame * 29, 32, 29, 16, self.x, self.y)

class Emy_Orange:
    def __init__(self):
        self.x, self.y = 210, 180
        self.frame = 4
        self.image = load_image('orange.png')

    def update(self):
        self.frame = (self.frame + 1) % 4


    def draw(self):
        self.image.clip_draw(self.frame * 29, 32, 29, 16, self.x, self.y)



def enter():
    global player, game_map
    global emy_Red, emy_Blue, emy_Pink, emy_Orange
    
    player = Player()
    game_map = Game_map()
    
    emy_Red = Emy_Red()
    emy_Blue = Emy_Blue()
    emy_Pink = Emy_Pink()
    emy_Orange = Emy_Orange()
    pass


def exit():
    game_world.claer()
    pass


def handle_events():
    player.handle_events(events)
    pass


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    pass


def draw():
    clear_canvas()

    for game_object in game_world.all_objects():
        game_object.draw()
    
    update_canvas()
    pass
