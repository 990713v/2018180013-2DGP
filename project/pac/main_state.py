import random
import json
import os

from pico2d import *

import game_framework
import title_state

os.chdir('resourse')

name = "MainState"

game_map = None
player = None

# < 적 오브젝트 >
emy_R = None
emy_B = None
emy_P = None

class Game_map:
    def __init__(self):
        self.image = load_image('coin_map.png')
        self.image2 = load_image('black.png')

    def draw(self):
        
        self.image2.draw(162, 174)
        self.image.draw(162, 174)


# < 적 오브젝트>
class Emy_R:
    def __init__(self):
        self.x, self.y = 162, 180
        self.frame = 4
        self.image = load_image('red.png')

    def update(self):
        self.frame = (self.frame + 1) % 4


    def draw(self):
        self.image.clip_draw(self.frame * 29, 32, 29, 16, self.x, self.y)


class Emy_B:
    def __init__(self):
        self.x, self.y = 191, 180
        self.frame = 4
        self.image = load_image('blue.png')

    def update(self):
        self.frame = (self.frame + 1) % 4


    def draw(self):
        self.image.clip_draw(self.frame * 29, 32, 29, 16, self.x, self.y)


class Emy_P:
    def __init__(self):
        self.x, self.y = 210, 180
        self.frame = 4
        self.image = load_image('pink.png')

    def update(self):
        self.frame = (self.frame + 1) % 4


    def draw(self):
        self.image.clip_draw(self.frame * 29, 32, 29, 16, self.x, self.y)



nowX, nowY = 0, 0

class Player:
    def __init__(self):
        self.x, self.y = 162, 110
        self.frame = 4
        self.locate = 0
        self.image = load_image('pacman.png')

    def update(self):
        self.frame = (self.frame + 1) % 4
        delay(0.1)

    def handle_events(self, event):
        global nowX, nowY
        events = get_events()

        for event in events:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                    nowX += 1
                    nowY = 0
                    self.locate = 1

                elif event.key == SDLK_LEFT:
                    nowX -= 1
                    nowY = 0
                    self.locate = 2

                elif event.key == SDLK_UP:
                    nowY += 1
                    nowX = 0
                    self.locate = 3

                elif event.key == SDLK_DOWN:
                    nowY -= 1
                    nowX = 0
                    self.locate = 4

        self.x += nowX * 5
        self.y += nowY * 5

    def draw(self):
        if self.locate <= 1: # 오른쪽
            self.image.clip_draw(self.frame * 29, 0, 29, 16, self.x, self.y)
        elif self.locate == 2: # 왼쪽
            self.image.clip_draw(self.frame * 29, 16, 29, 16, self.x, self.y)
        elif self.locate == 3: # 위쪽
            self.image.clip_draw(self.frame * 29, 48, 29, 16, self.x, self.y)
        elif self.locate == 4: # 아래쪽
            self.image.clip_draw(self.frame * 29, 32, 29, 16, self.x, self.y)

        # 범위체크 ( 값 수정해줄것)
        #if self.x < 190:
            #self.x = 310
       # if self.x > 310:
        #    self.x = 290



def enter():
    global player, game_map
    global emy_R, emy_B, emy_P
    
    player = Player()
    game_map = Game_map()
    
    emy_R = Emy_R()
    emy_B = Emy_B()
    emy_P = Emy_P()
    pass


def exit():
    global player, game_map
    global emy_R, emy_B, emy_P
    
    del(player)
    del(game_map)
    
    del(emy_R)
    del(emy_B)
    del(emy_P)
    pass


def handle_events():
   # events = get_events()
    player.handle_events(events)
    pass


def update():
    player.update()
    
    emy_R.update()
    emy_B.update()
    emy_P.update()
    pass


def draw():
    clear_canvas()
    game_map.draw()
    player.draw()
    
    emy_R.draw()
    emy_B.draw()
    emy_P.draw()
    
    update_canvas()
    pass
