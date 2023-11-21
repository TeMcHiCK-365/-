#создай игру "Лабиринт"!
from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 420 :
            self.rect.y += self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 300:
            self.direction = 'right'
        if self.rect.x >= 450:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed 
        else:
            self.rect.x += self.speed 
       
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1 ,color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x, self.rect.y))







win_wigth = 700
win_height = 500
window = display.set_mode((win_wigth, win_height))
display.set_caption('Лабиринт')
background = transform.scale(image.load('background.jpg'),(700,500))


mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
kick = mixer.Sound('kick.ogg')


font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN' ,True, (255, 215, 0))
lose = font.render('YOU LOSE',True, (180, 0, 0))

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

game = True
clock = time.Clock()
FPS = 60 
player = Player('hero.png', 5, 420, 4)
monster = Enemy('cyborg.png', 620, 280, 2)
final = GameSprite('treasure.png', 520, 420, 0)

wall_1 = Wall(188, 242, 0, 100, 20, 450,10)
wall_2 = Wall(188, 242, 0, 100, 480, 350,10)
wall_3 = Wall(188, 242, 0, 100, 20, 10,380)
finish = False

while game:
    window.blit(background,(0, 0))
    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0))

        wall_1.draw_wall()
        wall_2.draw_wall()
        wall_3.draw_wall()
        player.update()        
        player.reset()
        monster.reset()
        final.reset()
        monster.update()
        if sprite.collide_rect(player,final):
            player = Player('hero.png', 5, 420, 4)
            window.blit(win,(200, 200))
            finish = True
            money.play()
        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, wall_1) or sprite.collide_rect(player, wall_2) or sprite.collide_rect(player, wall_3):
            window.blit(lose,(200, 200))
            finish = True
            kick.play()

    clock.tick(FPS)     
    display.update()