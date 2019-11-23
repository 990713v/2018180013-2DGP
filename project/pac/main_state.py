import random
import json
import os

from pico2d import *
import game_framework
import game_world
import title_state

from player import Player
from game_map import Game_map
from coin import Coin, BigCoin

from emy_Red import Emy_Red
from emy_Blue import Emy_Blue
from emy_Pink import Emy_Pink
from emy_Orange import Emy_Orange

name = "MainState"
os.chdir('resourse')

player = None
game_map = None
coins = []
big_coins = []

emy_Red = None
emy_Blue = None
emy_Pink = None
emy_Orange = None

#count = 20


# 충돌체크
def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def enter():
    global game_map
    game_map = Game_map()
    game_world.add_object(game_map, 0)
            
    global player
    player = Player()
    game_world.add_object(player, 1)

    global coins, big_coins
    coins = [Coin() for i in range(10)]
    big_coins = [BigCoin() for i in range(10)]
    
    game_world.add_objects(coins, 1)
    game_world.add_objects(big_coins, 1)
    
    
    global emy_Red, emy_Blue, emy_Pink, emy_Orange
      
    emy_Red = Emy_Red()
    emy_Blue = Emy_Blue()
    emy_Pink = Emy_Pink()
    emy_Orange = Emy_Orange()

    game_world.add_object(emy_Red, 1)
    game_world.add_object(emy_Blue, 1)
    game_world.add_object(emy_Pink, 1)
    game_world.add_object(emy_Orange, 1)


def exit():
    game_world.claer()
    pass


def handle_events():
    player.handle_events(events)


def update():
    for game_objects in game_world.all_objects():
        game_objects.update()

    for coin in coins:
        if collide(player, coin):           
            game_world.remove_object(coin)

    for big_coin in big_coins:
        if collide(player, big_coin):
            game_world.remove_object(big_coin)
        

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()    
    update_canvas()
