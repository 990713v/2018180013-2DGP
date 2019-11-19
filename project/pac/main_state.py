import random
import json
import os

from pico2d import *
import game_framework
import game_world
import title_state

from player import Player
from game_map import Game_map

# 적
from emy_Red import Emy_Red
from emy_Blue import Emy_Blue
from emy_Pink import Emy_Pink
from emy_Orange import Emy_Orange

name = "MainState"
os.chdir('resourse') # 'resourse' 폴더에 있는 png 파일 가져옴

player = None
#game_map = None

# < 적 오브젝트 >
emy_Red = None
emy_Blue = None
emy_Pink = None
emy_Orange = None


def enter():
    global player #, game_map
    global emy_Red, emy_Blue, emy_Pink, emy_Orange
    
    player = Player()
    game_map = Game_map()
    
    emy_Red = Emy_Red()
    emy_Blue = Emy_Blue()
    emy_Pink = Emy_Pink()
    emy_Orange = Emy_Orange()

    game_world.add_object(game_map, 0)
    game_world.add_object(player, 1)

    game_world.add_object(emy_Red, 1)
    game_world.add_object(emy_Blue, 1)
    game_world.add_object(emy_Pink, 1)
    game_world.add_object(emy_Orange, 1)
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
