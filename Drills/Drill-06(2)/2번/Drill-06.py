from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

p1 = ((random.randint(-400, 400 + 1), (random.randint(-400, 400 + 1))))
p2 = ((random.randint(-400, 400 + 1), (random.randint(-400, 400 + 1))))
p3 = ((random.randint(-400, 400 + 1), (random.randint(-400, 400 + 1))))
p4 = ((random.randint(-400, 400 + 1), (random.randint(-400, 400 + 1))))
p5 = ((random.randint(-400, 400 + 1), (random.randint(-400, 400 + 1))))
p6 = ((random.randint(-400, 400 + 1), (random.randint(-400, 400 + 1))))
p7 = ((random.randint(-400, 400 + 1), (random.randint(-400, 400 + 1))))
p8 = ((random.randint(-400, 400 + 1), (random.randint(-400, 400 + 1))))
p9 = ((random.randint(-400, 400 + 1), (random.randint(-400, 400 + 1))))
p10 = ((random.randint(-400, 400 + 1), (random.randint(-400, 400 + 1))))

def handle_events():
    global running
    global x, y
    global end_x, end_y
    global nowX, nowY

    events = get_events()

    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            for i in range(0, 100, 2):
                # draw p1-p2
                for i in range(0, 100, 2):
                    t = i / 100
                    x = ((-t ** 3 + 2 * t ** 2 - t) * p4[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[0]
                         + (-3 * t ** 3 + 4 * t ** 2 + t) * p2[0] + (t ** 3 - t ** 2) * p3[0]) / 2
                    y = ((-t ** 3 + 2 * t ** 2 - t) * p4[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[1]
                         + (-3 * t ** 3 + 4 * t ** 2 + t) * p2[1] + (t ** 3 - t ** 2) * p3[1]) / 2

                # draw p2-p3
                for i in range(0, 100, 2):
                    t = i / 100
                    x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0]
                         + (-3 * t ** 3 + 4 * t ** 2 + t) * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
                    y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1]
                         + (-3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2

                # draw p3-p4
                for i in range(0, 100, 2):
                    t = i / 100
                    x = ((-t ** 3 + 2 * t ** 2 - t) * p2[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[0]
                         + (-3 * t ** 3 + 4 * t ** 2 + t) * p4[0] + (t ** 3 - t ** 2) * p1[0]) / 2
                    y = ((-t ** 3 + 2 * t ** 2 - t) * p2[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[1]
                         + (-3 * t ** 3 + 4 * t ** 2 + t) * p4[1] + (t ** 3 - t ** 2) * p1[1]) / 2

                # draw p4-p1
                for i in range(0, 100, 2):
                    t = i / 100
                    x = ((-t ** 3 + 2 * t ** 2 - t) * p3[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[0]
                         + (-3 * t ** 3 + 4 * t ** 2 + t) * p1[0] + (t ** 3 - t ** 2) * p2[0]) / 2
                    y = ((-t ** 3 + 2 * t ** 2 - t) * p3[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[1]
                         + (-3 * t ** 3 + 4 * t ** 2 + t) * p1[1] + (t ** 3 - t ** 2) * p2[1]) / 2


open_canvas(KPU_WIDTH, KPU_HEIGHT)
character = load_image('animation_sheet.png')
kpu_ground = load_image('KPU_GROUND.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
nowX, nowY = KPU_WIDTH // 2, KPU_HEIGHT // 2
end_x = nowX
end_y = nowY

frame = 0
show_cursor()

while running:
    move_x = (end_x - nowX) / 20
    move_y = (end_y - nowY) / 20
    nowX += move_x
    nowY += move_y

    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100, 100, 100, nowX, nowY)
    update_canvas()
    frame = (frame + 1) % 8

    delay(0.02)
    handle_events()

close_canvas()
