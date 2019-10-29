import game_framework
import main_state

from pico2d import *

name = "TitleState"
image = None


def enter():
    global image, image2
    image = load_image('start.png')
    image2 = load_image('black.png')


def exit():
    global image, image2
    del(image)
    del(image2)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)


def draw():
    clear_canvas()
    image2.draw(162, 174)
    image.draw(162, 174)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass