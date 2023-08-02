from pygame import *
window = display.set_mode((700, 500))
display.set_caption("Пинг понг")
window.fill((123, 104, 238))

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
