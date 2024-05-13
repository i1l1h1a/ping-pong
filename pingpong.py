from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image= transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

win_width = 600
win_height = 500
display.set_caption("pingpong")
window =display.set_mode ((win_width, win_height))
background = transform.scale(image.load("slika_pozadine.jpg"), (win_width, win_height))

class Player(GameSprite):
    def uptade_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 380:
            self.rect.y += self.speed

    def uptade_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 380:
            self.rect.y += self.speed

back = (200, 255, 255)
win_width = 600



ig1 = Player("racket.png", 530, 200, 5, 50, 150)
ig2 = Player("racket.png", 30, 200, 5, 50, 150)

game = True
finish = False
clock = time.Clock()
FPS = 60

ball = GameSprite("tennis ball.jpg", 380, 230, 3, 30, 30)
speed_x = 3
speed_y = 3

font.init()
font1 = font.Font(None, 30)
lose1 = font1.render("player 1 lose", True, (180,0,0))
lose2 = font1.render("player 2 lose", True, (180,0,0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    window.fill(back)

    if not finish:
        ball.reset()

        if ball.rect.y <= 0 or ball.rect.y >= 470:
            speed_y *= -1

        if sprite.collide_rect(ig1, ball) or sprite.collide_rect(ig2, ball):
            speed_x *= -1

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        ig1.uptade_r()
        ig2.uptade_l()
        ig1.reset()
        ig2.reset()

    if ball.rect.x < 0:
        finish = True
        window.blit(lose2, (230,250))

    if ball.rect.x > 600:
        finish = True
        window.blit(lose1, (230,250))

    display.update()
    clock.tick(FPS)