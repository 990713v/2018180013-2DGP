from pico2d import *
import game_world

nowX, nowY = 0, 0

class Player:
    def __init__(self):
        self.x, self.y = 324, 220
        self.frame = 4
        self.locate = 0
        self.image = load_image('pacman.png')

    def update(self):
        self.frame = (self.frame + 1) % 4
        self.x += nowX * 7
        self.y += nowY * 7
        delay(0.1)

    def handle_events(self, event):
        global nowX, nowY
        events = get_events()

        for event in events:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                    nowX += 1
                    self.locate = 1

                elif event.key == SDLK_LEFT:
                    nowX -= 1
                    self.locate = 2

                elif event.key == SDLK_UP:
                    nowY += 1
                    self.locate = 3

                elif event.key == SDLK_DOWN:
                    nowY -= 1
                    self.locate = 4

            elif event.type == SDL_KEYUP:
                if event.key == SDLK_RIGHT:
                    nowX -= 1
                elif event.key == SDLK_LEFT:
                    nowX += 1
                elif event.key == SDLK_UP:
                    nowY -= 1
                elif event.key == SDLK_DOWN:
                    nowY += 1

        #self.x += nowX * 5
        #self.y += nowY * 5

    def draw(self):
        if self.locate <= 1: # 오른쪽
            self.image.clip_draw(self.frame * 58, 0, 58, 32, self.x, self.y)
        elif self.locate == 2: # 왼쪽
            self.image.clip_draw(self.frame * 58, 32, 58, 32, self.x, self.y)
        elif self.locate == 3: # 위쪽
            self.image.clip_draw(self.frame * 58, 96, 58, 32, self.x, self.y)
        elif self.locate == 4: # 아래쪽
            self.image.clip_draw(self.frame * 58, 64, 58, 32, self.x, self.y)

        # 범위체크 ( 값 수정해줄것)
        if self.x < 115:
            self.x = 529
        if self.x > 530:
            self.x = 116
