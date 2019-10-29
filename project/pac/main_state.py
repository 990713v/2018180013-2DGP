import random
import json
import os

from pico2d import *

#open_canvas()

import game_framework
import start_state


name = "MainState"

player = None
game_map = None
emy_R = None


class Game_map:
    def __init__(self):
        self.image = load_image('coin_map.png')

    def draw(self):
        self.image.draw(400, 300)


class Player:
    def __init__(self):
        self.x, self.y = 400, 240
        self.frame = 4 #왜 5라 적혀있었지
        self.image = load_image('pacman.png')
        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 4 ####
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <=0:
            self.dir = 1


    def draw(self):
        self.image.clip_draw(self.frame * 29, 0, 29, 16, self.x, self.y)


        
class Emy_R:
    def __init__(self):
        self.x, self.y = 401, 320

    def update(self):
        self.frame = (self.frame + 1) % 4

    def draw(self):
        self.image.clip_draw(self.frame * 29, 48, 29, 16, self.x, self.y)


def enter():
    global game_map, player
    game_map = Game_map()
    player = Player()
    pass


def exit():
    global game_map, player

    del(game_map)
    del(player)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    pass


def update():
    player.update()
    pass


def draw():
    clear_canvas()
    game_map.draw()
    player.draw()
    update_canvas()
    pass