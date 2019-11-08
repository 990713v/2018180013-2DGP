from pico2d import *
import game_world

nowX, nowY = 0, 0

#적에게 닿았을때
class SleepState:
    @staticmethod
    def enter(player, event):
        player.frame = 0

    @staticmethod
    def do(player):
        player.frame = (player.frame+1)%4

    @staticmethod:
        def draw(player):
            player.image.clip_draw(player.frame*29

class Player:
    def __init__(self):
        self.x, self.y = 162, 110
        self.frame = 4
        self.locate = 0
        self.image = load_image('pacman.png')

    def update(self):
        self.frame = (self.frame + 1) % 4
        self.x += nowX * 5
        self.y += nowY * 5
        delay(0.1)

    def handle_events(self, event):
        global nowX, nowY
        events = get_events()

        for event in events:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                    nowX += 1
                    #nowY = 0
                    self.locate = 1

                elif event.key == SDLK_LEFT:
                    nowX -= 1
                    #nowY = 0
                    self.locate = 2

                elif event.key == SDLK_UP:
                    nowY += 1
                    #nowX = 0
                    self.locate = 3

                elif event.key == SDLK_DOWN:
                    nowY -= 1
                    #nowX = 0
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
            self.image.clip_draw(self.frame * 29, 0, 29, 16, self.x, self.y)
        elif self.locate == 2: # 왼쪽
            self.image.clip_draw(self.frame * 29, 16, 29, 16, self.x, self.y)
        elif self.locate == 3: # 위쪽
            self.image.clip_draw(self.frame * 29, 48, 29, 16, self.x, self.y)
        elif self.locate == 4: # 아래쪽
            self.image.clip_draw(self.frame * 29, 32, 29, 16, self.x, self.y)

        # 범위체크 ( 값 수정해줄것)
        #if self.x < 190:
            #self.x = 310
       # if self.x > 310:
        #    self.x = 290
