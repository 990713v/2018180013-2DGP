# ~ 1주차 ~
# 캐릭터의 x, y좌표를 담을 구조체 생성하기
# 맵 배열 생성 (벽과 길 구분, 벽은 1 길은 0으로)

from pico2d import *
open_canvas()

def handle_events():
    global nowX
    global nowY
    global locate
    events = get_events()

    for event in events:
        if event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                   nowX += 1
                   locate = 1
                elif event.key == SDLK_LEFT:
                   nowX -= 1
                   locate = 2
                elif event.key == SDLK_UP:
                   nowY += 1
                   locate = 3
                elif event.key == SDLK_DOWN:
                   nowY -= 1
                   locate = 4

        elif event.type == SDL_KEYUP:
                if event.key == SDLK_RIGHT:
                   nowX -= 1
                elif event.key == SDLK_LEFT:
                   nowX += 1
                elif event.key == SDLK_UP:
                   nowY -= 1
                elif event.key == SDLK_DOWN:
                   nowY += 1

map = load_image('coin_map.png')
emy1 = load_image('blue.png')  # 너비 테스트 29*16
player = load_image('pacman.png')
# 리소스 테스트
player2 = load_image('pac_die.png')

x = 400
y = 240

frame = 5
nowX = 0
nowY = 0
locate = 0

while 1:
        clear_canvas()
        map.draw(400, 300)  # 맵 띄우기

        handle_events()
        if locate <= 1: # 오른쪽
            player.clip_draw(frame * 29, 0, 29 ,16, x, y)
        elif locate == 2: # 왼쪽
            player.clip_draw(frame * 29, 16, 29, 16, x, y)
        elif locate == 3: #위쪽
            player.clip_draw(frame * 29, 48, 29, 16, x, y)
        elif locate == 4: #아래쪽
            player.clip_draw(frame * 29, 32, 29, 16, x, y)
        update_canvas()

        frame = (frame + 1) % 8
        x += nowX * 5
        y += nowY * 5
        delay(0.1)

close_canvas()