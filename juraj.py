from pygame import *

win_width = 500
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("PONG!")

game = True

class Player():
    def __init__(self, x_pos, up_key, down_key):
        self.x = x_pos
        self.y = win_height / 2
        self.up = up_key
        self.down = down_key
        self.image = Surface((5, 50))
        self.image.fill((255, 255, 255))

    def update(self):
        keys = key.get_pressed()
        if (keys[self.up]):
            self.y -= 0.5
        if (keys[self.down]):
            self.y += 0.5

    def reset(self):
        window.blit(self.image, (self.x, self.y))
        

playerR = Player(100, K_w, K_s)

while game:
    for e in event.get():
       if e.type == QUIT:
           game = False
    
    playerR.update()
    playerR.reset()

    window.fill((0, 0, 0))

    display.update()