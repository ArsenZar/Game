import pygame
import random
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

FPS = pygame.time.Clock()

HEIGHT = 800
WIDTH = 1200

FONT = pygame.font.SysFont('Verdana', 20)

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_BONUS = (0, 150, 150)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

bg = pygame.transform.scale(pygame.image.load('background.png'), (WIDTH, HEIGHT))
bg_X1 = 1
bg_X2 = bg.get_width()
bg_move = 3

player_size = (20,20)
spawn_position = (50, (HEIGHT/2)-50)
player = pygame.image.load('player.png').convert_alpha() #pygame.Surface(player_size)
player_rect = player.get_rect(topleft = spawn_position)
# player_speed = [5, 5]
player_move_down = [0, 5]
player_move_right = [5, 0]
player_move_up = [0, -5]
player_move_left = [-5, 0]

# def create_enemy():
#     enemy_size = (35, 35)
#     enemy = pygame.image.load('enemy.png') #pygame.Surface(enemy_size)
#     enemy_rect = pygame.Rect(WIDTH, random.randint(0, HEIGHT), *enemy_size)
#     enemy_move = [random.randint(-8, -4), 0]
#     return [enemy, enemy_rect, enemy_move]

def create_enemy():
    enemy_size = (20, 20)
    enemy = pygame.image.load('enemy.png').convert_alpha()
    
    min_y = 50 
    max_y = HEIGHT - 50 - enemy_size[1] 
    
    enemy_rect = pygame.Rect(WIDTH, random.randint(min_y, max_y), *enemy.get_size()) 
    enemy_move = [random.randint(-4, -1), 0]  # Рух вліво
    
    return [enemy, enemy_rect, enemy_move]


# def create_bonus():
#     bonus_size = (10, 10)
#     bonus = pygame.image.load('bonus.png')
#     bonus_rect = pygame.Rect(random.randint(0, WIDTH - bonus_size[0]), 0, *bonus_size)  # y = 0
#     bonus_move = [0, random.randint(1, 4)]  # Рух вниз з випадковою швидкістю
#     return [bonus, bonus_rect, bonus_move]

def create_bonus():
    bonus_size = (10, 10)
    bonus = pygame.image.load('bonus.png').convert_alpha()
    
    min_x = 50  
    max_x = WIDTH - 50 - bonus_size[0]  
    
    bonus_rect = pygame.Rect(random.randint(min_x, max_x), 0, *bonus.get_size()) 
    bonus_move = [0, random.randint(1, 4)]  # Рух вниз

    return [bonus, bonus_rect, bonus_move]



CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 2000)

CREATE_BONUS = pygame.USEREVENT + 5
pygame.time.set_timer(CREATE_BONUS, 5000)

enemies = []
benefits = [] 

score = 0


playing = True

while playing:
    FPS.tick(120)

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            benefits.append(create_bonus())

    bg_X1 -= bg_move
    bg_X2 -= bg_move

    if bg_X1 < -bg.get_width():
        bg_X1 = bg.get_width()

    if bg_X2 < -bg.get_width():
        bg_X2 = bg.get_width()

    main_display.blit(bg, (bg_X1, 0))
    main_display.blit(bg, (bg_X2, 0))

    keys = pygame.key.get_pressed()

    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move(player_move_down)

    if keys[K_RIGHT] and player_rect.right < WIDTH:
        player_rect = player_rect.move(player_move_right)

    if keys[K_UP] and player_rect.top > 0:
        player_rect = player_rect.move(player_move_up)

    if keys[K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(player_move_left)

    for enemy in enemies:
        enemy[1] = enemy[1].move(enemy[2])
        main_display.blit(enemy[0], enemy[1])

        if player_rect.colliderect(enemy[1]):
            playing = False

    for bonus in benefits:
        bonus[1] = bonus[1].move(bonus[2])
        main_display.blit(bonus[0], bonus[1])

        if player_rect.colliderect(bonus[1]):
            score+=1
            benefits.pop(benefits.index(bonus))
   
    main_display.blit(FONT.render(str(score), True, COLOR_BLACK), (WIDTH-50, 20))
    main_display.blit(player, player_rect)

    # print(len(benefits))

    pygame.display.flip()

    for enemy in enemies:
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))

    for bonus in benefits:
        if bonus[1].bottom > HEIGHT:
            benefits.pop(benefits.index(bonus))


# new commit (test in 2 files both)