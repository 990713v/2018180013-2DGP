# ~ 1주차 ~
# 캐릭터의 x, y좌표를 담을 구조체 생성하기
# 맵 배열 생성 (벽과 길 구분, 벽은 1 길은 0으로)

from pico2d import *

open_canvas()

map = load_image('original_map.png')
emy1 = load_image('red.png') # 너비 테스트 29*16
player = load_image('pacman.png')
#리소스 테스트
player2 = load_image('pac_die.png')

x= 280
x2 = 280
y = 300
y2 = 300
frame = 5
n = 0

while 1:
        while n < 15:
                clear_canvas()
                map.draw(400, 300) # 맵 띄우기
                player.clip_draw(frame * 29, 48, 29, 16, 280, y) # 팩맨 위
                player.clip_draw(frame * 29, 32, 29, 16, 280, y2) # 팩맨 아
                player.clip_draw(frame * 29, 16, 29, 16, x2, 260) # 팩맨 왼
                player.clip_draw(frame * 29, 0, 29, 16, x, 260) # 팩맨 오

                update_canvas()
                frame = (frame+1)%8
                delay(0.08)
        
                x += 1
                y += 1
                x2 -= 1
                y2 -= 1
                n += 1
        
                get_events()
                
        while n >= 0:
                clear_canvas()
                map.draw(400, 300) # 맵 띄우기
                player2.clip_draw(frame * 16, 0, 16, 16, 320, 300)
                update_canvas()
                frame = (frame+1)%8
                delay(0.15)
                n -=0.2
        

close_canvas()
n
