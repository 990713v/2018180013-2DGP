from pico2d import *

import game_framework
import main_state

name = "TitleState"
image = None
background = None

def enter():
    global image, background
    image = load_image('start.png')
    background = load_image('black.png')


def exit():
    global image, background
    del(image)
    del(background)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
                #print("ddd")
                game_framework.change_state(main_state)


def draw():
    clear_canvas()
    background.draw(324, 348)
    image.draw(324, 348)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass
