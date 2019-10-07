from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global x, y
    global nowX, nowY  # 캐릭터 좌표

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type  == SDL_MOUSEBUTTONDOWN:
            while nowX == x:
                nowX, nowY = event.x, KPU_HEIGHT - 1 - event.y

        elif event.type == SDL_MOUSEMOTION: #마우스 모션이벤트 감지
            x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
pointer = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor() # 마우스 커서 숨김. show_cursor() 는 커서 아이콘 출력
nowX, nowY = x, y
while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    pointer.draw(x, y)
    if(nowX <= x):
        character.clip_draw(frame * 100, 0, 100, 100, nowX, nowY)
    elif(nowX > x):
        character.clip_draw(frame * 100, 100, 100, 100, nowX, nowY)
    update_canvas()
    frame = (frame + 1) % 8

    delay(0.02)
    handle_events()

close_canvas()




