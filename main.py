from random import randint
from re import L
from pygame import *
win_width = 800
win_height = 600
font.init()
font1 = font.SysFont('Arial', 80)
player1win = font1.render('Player 1 won!', True, (50, 168, 82))
player2win = font1.render('Player 2 won!', True, (50, 168, 82))
window = display.set_mode((win_width, win_height))
display.set_caption("Пінг-Понг")
background = transform.scale(image.load("bg.png"), (win_width, win_height))
FPS = 60
clock = time.Clock()

class GameSprite(sprite.Sprite):
  # конструктор класу
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # викликаємо конструктор класу (Sprite):
        sprite.Sprite.__init__(self)

        # кожний спрайт повиннен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # кожний спрайт спрайт зберігає властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
  # метод, який малює героя на вікні
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# клас головного героя
class Player(GameSprite):
    # метод для керування спрайтом стрілками клавіатури
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 165:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 165:
            self.rect.y += self.speed
  # метод "постріл" (використовуємо місце гравця, щоб створити там кулю)
class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # кожний спрайт спрайт зберігає властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.velocity = [randint(4,8),randint(-8,8)]
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
    def hit(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)

player1 = Player("white.png", 5, win_height/2, 20, 150, 5)
player2 = Player("white.png", 775, win_height/2, 20, 150, 5)
ball = Ball("ball.png", win_width/2, win_height/2, 60, 60, 5)
game = True
finish = False
while game:
    keys = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0,0))
        player1.update_l()
        player1.reset()
        player2.update_r()
        player2.reset()
        ball.reset()
        ball.update()
        if ball.rect.x >= win_width- 40:
            window.blit(player2win, (200, 200))
            finish = True
        if ball.rect.x<= win_width - 840:
            window.blit(player1win, (200, 200))
            finish = True
        if ball.rect.y>540:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y<0:
            ball.velocity[1] = -ball.velocity[1]
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            ball.hit()
        display.update()
    if keys[K_r]:
        ball.rect.x = win_width/2
        ball.rect.y = win_height/2
        player1.rect.x = 5
        player2.rect.x = 775 
        player1.rect.y = win_height/2
        player1.rect.y = win_height/2
        finish = False      
    clock.tick(FPS)