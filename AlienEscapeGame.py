import pygame
import random
import sys
import cv2
from pygame import mixer



pygame.init()

WIDTH = 800
HEIGHT = 600

SPEED = 10

screen = pygame.display.set_mode((WIDTH,HEIGHT))

mixer.music.load('background_music.mp3')
mixer.music.play(-1)

backgroundImg = pygame.image.load('universe.jpg')

player_size = 50
playerImg = pygame.image.load('ufo_icon.png')
player_pos = [370, 480]

enemy_size = 50
enemyImg = pygame.image.load('torpedo.png')
enemy_pos = [random.randint(0,WIDTH - enemy_size),0]
enemy_list = [enemy_pos]

you_win = pygame.image.load('Win.jpeg')
you_lose = pygame.image.load('GameOver.jpeg')

score = 0
YELLOW = (255,255,0)
GREY = (127,127,127)

title_font = pygame.font.Font('Minecrafter.Reg.ttf', 34)
titleX = 270
titleY = 10

def show_title(x,y):
    title = title_font.render("ALIEN ESCAPE", True, GREY)
    screen.blit(title, (x, y))

def background():
    screen.blit(backgroundImg, (0,0))
def player():
    screen.blit(playerImg, (player_pos))
def enemy():
    screen.blit(enemyImg, (enemy_pos))



game_over = False

clock = pygame.time.Clock()

myFont = pygame.font.SysFont("monospace", 35)

def set_level(score, SPEED):
    if score <= 20:
        SPEED = 5
    elif score < 40:
        SPEED = 8
    elif score < 60:
        SPEED = 12
    else:
        SPEED = 15
    return SPEED


def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.1:
        x_pos = random.randint(0, WIDTH - enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])


def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        screen.blit(enemyImg, (enemy_pos))



def update_enemy_positions(enemy_list, score):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
            enemy_pos[1] += SPEED
        else:
            enemy_list.pop(idx)
            score += 1
    return score


def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos, player_pos):
            return True
    return False


def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]
    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y+enemy_size)):
            return True

    return False


while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]
            if event.key == pygame.K_LEFT:
                x -= player_size
            if event.key == pygame.K_RIGHT:
                x += player_size
            player_pos = [x,y]


    screen.fill((0,0,0))
    background()
    show_title(titleX, titleY)
    drop_enemies(enemy_list)
    score  = update_enemy_positions(enemy_list, score)
    SPEED = set_level(score,SPEED)
    text = "Score:" + str(score)
    label = myFont.render(text, 1, YELLOW)
    screen.blit(label, (WIDTH-200, HEIGHT-40))
    draw_enemies(enemy_list)
    player()
    clock.tick(30)

    if collision_check(enemy_list, player_pos):
        screen.blit(you_lose, (0, 0))
        game_over = True
    if score == 100:
        screen.blit(you_win, (0, 0))
        game_over = True

    pygame.display.update()



