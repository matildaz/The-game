import pygame

pygame.init()
# создаем игровое окно
win = pygame.display.set_mode((1000,700))
# заголовок
pygame.display.set_caption("Игра на питоне")

walk_right = [pygame.image.load('Sprites/pygame_right_1.png'),
pygame.image.load('Sprites/pygame_right_2.png'),pygame.image.load('Sprites/pygame_right_3.png'),
pygame.image.load('Sprites/pygame_right_4.png'),pygame.image.load('Sprites/pygame_right_5.png'),
pygame.image.load('Sprites/pygame_right_6.png')]

walk_left = [pygame.image.load('Sprites/pygame_left_1.png'),
pygame.image.load('Sprites/pygame_left_2.png'),pygame.image.load('Sprites/pygame_left_3.png'),
pygame.image.load('Sprites/pygame_left_4.png'),pygame.image.load('Sprites/pygame_left_5.png'),
pygame.image.load('Sprites/pygame_left_6.png')]

play_stand = pygame.image.load('Sprites/pygame_idle.png')

class snaryad():
    def __init__(self,x,y,r,colour,direction):
        self.x = x
        self.y = y
        self.r = r
        self.colour = colour
        self.direction = direction
        self.bulletSpeed = 8 * direction

    def draw(self, win):
        pygame.draw.circle(win,self.colour,(self.x,self.y),self.r)

clock = pygame.time.Clock()

def lowSpeed():
    global speed
    if speed > 5:
        speed -= 5

def drawWindow():
    global aimCount
     # после каждого перемещения нужно заполнять поле черным цветом
    win.fill((0,0,0))
    # создание объекта
    if aimCount + 1 >= 30:
        aimCount = 0
    if left:
        win.blit(walk_left[aimCount // 5], (x, y))
        aimCount += 1
    elif right:
        win.blit(walk_right[aimCount // 5], (x, y))
        aimCount += 1
    else:
        win.blit(play_stand, (x, y))
    for bullet in bullets:
        bullet.draw(win)

    #pygame.draw.rect(win,(0,0,255),(x,y,width,height))
    pygame.display.update()

#параметры
x = 50
y : float = 700 - 76
width = 60
height = 71
speed = 5
speedCount = 10

isJump = False
jumpCount = 10
aimCount = 0

right = False
left = False

bullets : list = []
lastMove = 'right'
direction = 1
#coolDown = 0

WHITE = (255, 255, 255)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)

# цикл самой игры
run = True
while run:
    # время через которое цикл будет обновляться
    clock.tick(30)

    for bullet in bullets:
        if bullet.x < 1000 and bullet.x > 0:
            bullet.x += bullet.bulletSpeed
        else:
            bullets.pop(bullets.index(bullet))

    # опишем структуру выхода из программы
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # отслеживание нажатий 
    keys = pygame.key.get_pressed()

    # определение последнего направления
    if lastMove == 'right':
        direction = 1
    else:
        direction = -1

    # запуск снаряда
    if keys[pygame.K_f]:
        if len(bullets) < 10:
                bullets.append(snaryad(round(x + width // 2), round(y + height // 2), 
                5, RED, direction))

            
    # управление персонажем
    if keys[pygame.K_LSHIFT]:
        speed += 5
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
        lastMove = 'left'
    elif keys[pygame.K_RIGHT] and x < 1000 - width - 5:
        x += speed
        left = False
        right = True
        lastMove = 'right'
    else:
        left = False
        right = False
        aimCount = 0
    if not(isJump):
        if keys[pygame.K_UP]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    lowSpeed()
    drawWindow()

    
# на случай если программа не вышла прописываем функцию выхода еще раз
pygame.quit()
# %%
