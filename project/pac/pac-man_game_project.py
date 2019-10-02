# ~ 1주차 ~
# 캐릭터의 x, y좌표를 담을 구조체 생성하기
# 맵 배열 생성 (벽과 길 구분, 벽은 1 길은 0으로)

#import os
#os.chdir('C:\\Users\\10575\\Documents\\GitHub\\2018180013-2DGP\\project')
from pico2d import *

open_canvas()

map = load_image('pac_map.png')
map.draw(400,100,500,250)
