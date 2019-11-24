from pico2d import *
import game_world

class Score:
    def __init__(self):
        self.x, self.y = 239, 648
        self.score = 0
        self.font = load_font('ENCR10B.TTF', 30)

    def update(self):
        self.x = self.x
        pass

    def draw(self):
        self.font.draw(self.x, self.y, 'Score: %d' % self.score, (255, 255, 255))
