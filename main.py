from pygame import *
window = display.set_mode((700, 500))
display.set_caption("Пинг понг")
fon = transform.scale(image.load('background.jpg'), (700, 500))

class GameSprite(sprite.Sprite):
   def __init__(self, image_name, x, y , speed, size_x, size_y):
      super().__init__()
      self.image = transform.scale(image.load(image_name), (size_x, size_y))
      self.speed = speed
      self.rect = self.image.get_rect()
      self.rect.x = x
      self.rect.y = y
   def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 5: 
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 470: 
            self.rect.y += self.speed

    def update2(self):
            keys_pressed = key.get_pressed()

            if keys_pressed[K_UP] and self.rect.y > 5: 
                self.rect.y -= self.speed
            if keys_pressed[K_DOWN] and self.rect.y < 470: 
                self.rect.y += self.speed

rocet = Player('racket.png',50, 50, 15, 40, 70)
rocet2 = Player('racket.png',650, 50, 15, 40, 70)
boll = GameSprite('ball.png', 123, 232, 0, 20, 20)

speed_x = 3
speed_y = 3

finish = False

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish == False:
        window.blit(fon,(0,0))
        rocet.update()
        rocet.reset()
        rocet2.update2()
        rocet2.reset()
        boll.rect.x += speed_x
        boll.rect.y += speed_y
        boll.reset()
    if boll.rect.y > 480 or boll.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(rocet, boll)or sprite.collide_rect(rocet2, boll):
        speed_x *= -1
    time.delay(50)
    display.update()

