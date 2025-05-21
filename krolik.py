import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

# Здесь мы будем рисовать
def draw_hare(surface, x, y, width, height, color):
  '''
  Рисует зайца на экране.
  surface - объект pygame.Surface
  x, y - координаты левого верхнего угла изображения
  width, height - ширина и высота изобажения
  color - цвет, заданный в формате, подходящем для pygame.Color
  '''
  body_width = width // 2
  body_height = height // 2
  body_y = y + body_height // 2
  draw_body(surface, x, body_y, body_width, body_height, color)

  head_size = height // 4
  draw_head(surface, x, y - head_size // 2, head_size, color)

  ear_height = height // 3
  ear_y = y - height // 2 + ear_height // 2
  for ear_x in (x - head_size // 4, x + head_size // 4):
      draw_ear(surface, ear_x, ear_y, width // 8, ear_height, color)

  leg_height = height // 16
  leg_y = y + height // 2 - leg_height // 2
  for leg_x in (x - width // 4, x + width // 4):
      draw_leg(surface, leg_x, leg_y, width // 4, leg_height, color)

  ear_height1 = height // 7
  ear1_y = y - height // 4 + ear_height // 7
  for ear1_x in (x - head_size // 7, x + head_size - 64):
      draw_ear1(surface, ear1_x, ear1_y, width // 9, ear_height1, color)

  nose_size = head_size // 14
  nose_y = y - head_size // 2 + head_size // 4
  draw_nose(surface, x, nose_y, nose_size, (229, 34, 174))


  glasses_x = x - head_size // 13
  glasses_y = y - head_size  + head_size // 3
  draw_glasses(surface,  glasses_x,glasses_y )

  draw_eyes(surface, x - head_size // 5, y - head_size +30 + head_size // 4)
  draw_eyes(surface, x + head_size // 4, y - head_size +30 + head_size // 4)

  draw_arms(surface, x, y, body_width, body_height)

def draw_arms(surfase, x, y, width, height):
    '''Рисуер лапу зайца
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    '''
    ellipse(surfase, (255, 250, 250), (x - width // 1.7, y + height / 10, width // 2, height // 2))
    ellipse(surfase, (255, 250, 250), (x + width // 20, y + height / 10, width // 2, height // 2))



def draw_eyes(surface, x, y):
      ''' Рисует глаз зайца
       surface - объект pygame.Surface
      x, y - координаты центра изображения'''
      eye_size = 6
      circle(surface, (91, 75, 196), (x + eye_size // 2, y), eye_size)# можно добавить переменную цвета
      circle(surface, (0,0,0), (x + eye_size // 2, y), eye_size-1)# зрачок



def draw_glasses(surface, x, y):
    ''' Рисует бровь зайца
     surface - объект pygame.Surface
      x, y - координаты центра изображения'''
    glasses_width = 70
    glasses_height = 10
    rect(surface, (0, 0, 0), (x - glasses_width//2 + glasses_height//2 , y - glasses_height//2 , glasses_width , glasses_height)) # бровь



def draw_body(surface, x, y, width, height, color):
      '''
      Рисует тело зайца.
      surface - объект pygame.Surface
      x, y - координаты центра изображения
      width, height - ширина и высота изобажения
      color - цвет, заданный в формате, подходящем для pygame.Color
      '''
      ellipse(surface, color, (x - width // 2, y - height // 2, width, height))




def draw_head(surface, x, y, size, color):
      '''
      Рисует голову зайца.
      surface - объект pygame.Surface
      x, y - координаты центра изображения
      size - диаметр головы
      color - цвет, заданный в формате, подходящем для pygame.Color
      '''
      circle(surface, color, (x, y+3), size //2)

def draw_ear(surface, x, y, width, height, color):
      '''
      Рисует ухо зайца.
      surface - объект pygame.Surface
      x, y - координаты центра изображения
      width, height - ширина и высота изобажения
      color - цвет, заданный в формате, подходящем для pygame.Color
      '''
      ellipse(surface, color, (x - width // 2, y - height // 2, width, height))

def draw_leg(surface, x, y, width, height, color):
      '''
      Рисует ногу зайца.
      surface - объект pygame.Surface
      x, y - координаты центра изображения
      width, height - ширина и высота изобажения
      color - цвет, заданный в формате, подходящем для pygame.Color
      '''
      ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_ear1(surface, x, y, width, height, color):
    '''
    Рисует внутри уха зайца.
    surface - объект pygame.Surface
    x, y - координаты

Припизднутый Скулбойчик, [21.05.2025 20:08]
центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    ellipse(surface, (199, 66, 186), (x - width , y - height , width, height))

def draw_nose(surface, x, y, size, color):
    ''' Рисует нос зайца
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
     '''
    circle(surface, color, (x, y), size)



draw_hare(screen, 200, 200, 200, 400, (200, 200, 200))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
