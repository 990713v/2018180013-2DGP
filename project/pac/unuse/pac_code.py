
# 시작 좌표

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

    
while 1:
        #clear_canvas()
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
        #update_canvas()

        # 범위 체크
        if x < 290:
            x = 510
        if x > 510:
            x = 290

        frame = (frame + 1) % 4
        x += nowX * 5
        y += nowY * 5
        delay(0.1)



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




     

#close_canvas()
