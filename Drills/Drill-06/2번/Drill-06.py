from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def curve(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
    global nowX, nowY
    # draw p1-p2
    for i in range(0, 100, 2):
        t = i / 100
        nowX = ((-t**3 + 2*t**2 - t)*p10[0] + (3*t**3 - 5*t**2 + 2)*p1[0] + (-3*t**3 + 4*t**2 + t)*p2[0] + (t**3 - t**2)*p3[0])/2
        nowY = ((-t**3 + 2*t**2 - t)*p10[1] + (3*t**3 - 5*t**2 + 2)*p1[1] + (-3*t**3 + 4*t**2 + t)*p2[1] + (t**3 - t**2)*p3[1])/2

    # draw p2-p3
    for i in range(0, 100, 2):
        t = i / 100
        nowX = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        nowY = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2

    # draw p3-p4
    for i in range(0, 100, 2):
        t = i / 100
        nowX = ((-t**3 + 2*t**2 - t)*p2[0] + (3*t**3 - 5*t**2 + 2)*p3[0] + (-3*t**3 + 4*t**2 + t)*p4[0] + (t**3 - t**2)*p5[0])/2
        nowY = ((-t**3 + 2*t**2 - t)*p2[1] + (3*t**3 - 5*t**2 + 2)*p3[1] + (-3*t**3 + 4*t**2 + t)*p4[1] + (t**3 - t**2)*p5[1])/2


    # draw p4-p5
    for i in range(0, 100, 2):
        t = i / 100
        nowX = ((-t**3 + 2*t**2 - t)*p3[0] + (3*t**3 - 5*t**2 + 2)*p4[0] + (-3*t**3 + 4*t**2 + t)*p5[0] + (t**3 - t**2)*p6[0])/2
        nowY = ((-t**3 + 2*t**2 - t)*p3[1] + (3*t**3 - 5*t**2 + 2)*p4[1] + (-3*t**3 + 4*t**2 + t)*p5[1] + (t**3 - t**2)*p6[1])/2


    # draw p5-p6
    for i in range(0, 100, 2):
        t = i / 100
        nowX = ((-t**3 + 2*t**2 - t)*p4[0] + (3*t**3 - 5*t**2 + 2)*p5[0] + (-3*t**3 + 4*t**2 + t)*p6[0] + (t**3 - t**2)*p7[0])/2
        nowY = ((-t**3 + 2*t**2 - t)*p4[1] + (3*t**3 - 5*t**2 + 2)*p5[1] + (-3*t**3 + 4*t**2 + t)*p6[1] + (t**3 - t**2)*p7[1])/2

    # draw p6-p7
    for i in range(0, 100, 2):
        t = i / 100
        nowX = ((-t**3 + 2*t**2 - t)*p5[0] + (3*t**3 - 5*t**2 + 2)*p6[0] + (-3*t**3 + 4*t**2 + t)*p7[0] + (t**3 - t**2)*p8[0])/2
        nowY = ((-t**3 + 2*t**2 - t)*p5[1] + (3*t**3 - 5*t**2 + 2)*p6[1] + (-3*t**3 + 4*t**2 + t)*p7[1] + (t**3 - t**2)*p8[1])/2

    # draw p7-p8
    for i in range(0, 100, 2):
        t = i / 100
        nowX = ((-t**3 + 2*t**2 - t)*p6[0] + (3*t**3 - 5*t**2 + 2)*p7[0] + (-3*t**3 + 4*t**2 + t)*p8[0] + (t**3 - t**2)*p9[0])/2
        nowY = ((-t**3 + 2*t**2 - t)*p6[1] + (3*t**3 - 5*t**2 + 2)*p7[1] + (-3*t**3 + 4*t**2 + t)*p8[1] + (t**3 - t**2)*p9[1])/2

    # draw p8-p9
    for i in range(0, 100, 2):
        t = i / 100
        nowX = ((-t**3 + 2*t**2 - t)*p7[0] + (3*t**3 - 5*t**2 + 2)*p8[0] + (-3*t**3 + 4*t**2 + t)*p9[0] + (t**3 - t**2)*p10[0])/2
        nowY = ((-t**3 + 2*t**2 - t)*p7[1] + (3*t**3 - 5*t**2 + 2)*p8[1] + (-3*t**3 + 4*t**2 + t)*p9[1] + (t**3 - t**2)*p10[1])/2

    # draw p9-p10
    for i in range(0, 100, 2):
        t = i / 100
        nowX = ((-t**3 + 2*t**2 - t)*p8[0] + (3*t**3 - 5*t**2 + 2)*p9[0] + (-3*t**3 + 4*t**2 + t)*p10[0] + (t**3 - t**2)*p1[0])/2
        nowY = ((-t**3 + 2*t**2 - t)*p8[1] + (3*t**3 - 5*t**2 + 2)*p9[1] + (-3*t**3 + 4*t**2 + t)*p10[1] + (t**3 - t**2)*p1[1])/2

    # draw p10-p1
    for i in range(0, 100, 2):
        t = i / 100
        nowX = ((-t**3 + 2*t**2 - t)*p9[0] + (3*t**3 - 5*t**2 + 2)*p10[0] + (-3*t**3 + 4*t**2 + t)*p1[0] + (t**3 - t**2)*p2[0])/2
        nowY = ((-t**3 + 2*t**2 - t)*p9[1] + (3*t**3 - 5*t**2 + 2)*p10[1] + (-3*t**3 + 4*t**2 + t)*p1[1] + (t**3 - t**2)*p2[1])/2


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

# (random.randint(-400, 400), random.randint(-400, 400)) 랜덤좌표

while running:
    move_x = (end_x - nowX) / 20
    move_y = (end_y - nowY) / 20
    nowX += move_x
    nowY += move_y

    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100, 100, 100, nowX, nowY)

    frame = (frame + 1) % 8

    update_canvas()
    delay(0.02)

close_canvas()
