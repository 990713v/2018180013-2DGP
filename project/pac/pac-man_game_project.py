# ~ 1주차 10/03 ~

# 구현 완료한 것
# - 리소스 수정(캐릭터, 적)
# - 캐릭터 오브젝트 키 입력에 따른 행동+이미지(상하좌우)

# 해야할 것
# 맵 수정. 벽과 길 구분 , 충돌체크.  코인
# 캐릭터 죽을 때
# 클래스 ?

# 확인해볼 것
# 적 오브젝트 이동방향에 따른 모양 (o)


import random
from pico2d import *
open_canvas()

# 리소스
game_map = load_image('coin_map.png')
player = load_image('pacman.png')
player_die = load_image('pac_die.png')

# 시작 좌표
x = 400
y = 240

emy_RX = 401
emy_RY = 320

frame = 5

nowX = 0
nowY = 0
locate = 0


# 키 입력 함수
def handle_events():
    global nowX
    global nowY
    global locate
    
    events = get_events()

    for event in events:
        if locate != -1 and event.type == SDL_KEYDOWN:
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



# 적AI 함수 테스트 - 방향에 따른 이미지
# 프레임 당 크기 29*16
def emy_R():
    global emy_RX
    global emy_RY

    emy_R = load_image('red.png')
    #emy_R.clip_draw(frame * 29, 0, 29, 16, emy_RX, emy_RY)
    if(random.randrange(0, 3) == 0):
        emy_R.clip_draw(frame * 29, 48, 29, 16, emy_RX, emy_RY)
        emy_RX +=3
        
    elif(random.randrange(0, 3) == 1):
        emy_R.clip_draw(frame * 29, 32, 29, 16, emy_RX, emy_RY) 
        
    elif(random.randrange(0, 3) == 2):
        emy_R.clip_draw(frame * 29, 0, 29, 16, emy_RX, emy_RY)
        emy_RY -= 3
            
    elif(random.randrange(0, 3) == 3):
        emy_R.clip_draw(frame * 29, 16, 29, 16, emy_RX, emy_RY)
        emy_RY += 3



while 1:
        clear_canvas()
        game_map.draw(400, 300)  # 맵 띄우기
        emy_R() # 적AI 함수

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

        # 범위 체크
        if x < 290:
            x = 510
        if x > 510:
            x = 290

        frame = (frame + 1) % 4
        x += nowX * 5
        y += nowY * 5
        delay(0.1)


        
            

close_canvas()
