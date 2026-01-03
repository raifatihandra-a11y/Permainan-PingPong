from pygame import *

win_width = 700
win_height = 500
window = display.set_mode((700, 500))
background = transform.scale(image.load('parkinglot.png'), (win_width, win_height))
clock = time.Clock()
FPS = 60

class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Gamesprite):
    def motion_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 20:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y > -80:
            self.rect.y += self.speed

    def motion_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 20:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y > -80:
            self.rect.y += self.speed



racket_l = Player('mobilrackethijau.png', 3, 250, 165, 165, 6)
racket_r = Player('mobilracket.png', 560, 250, 165, 165, 6)
ball = Gamesprite('ball.png', 350, 250, 30, 30, 2)
speed_x = 5
speed_y = 6
font.init()
font1 = font.Font(None, 55)
lose1 = font1.render('PLAYER 1 LOSE!', True, (100, 0, 0))
lose2 = font1.render('PLAYER 2 LOSE!', True, (100, 0, 0))
finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        window.blit(background, (0, 0))
        racket_l.show()
        racket_l.motion_l()
        racket_r.show()
        racket_r.motion_r()
        ball.show()
        # untuk membuat bola bergerak
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        # untuk memantulkan bola disisi atas dan bawah
        if ball.rect.y > win_height-20 or ball.rect.y < 0:
            speed_y *= -1
        # untuk memantulkan bola di sisi atas dan bawah
        if sprite.collide_rect(racket_l, ball) or sprite.collide_rect(racket_r, ball):
            speed_x *= -1
        # untuk kondisi ketika bola menyentuh sisi kiri
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
        # untuk kondisi ketika bola menyentuh sisi kanan
        if ball.rect.x > 700:
            finish = True
            window.blit(lose2, (200, 200))
    display.update()
    clock.tick(FPS)



    
