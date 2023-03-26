import socket
import pygame
from Constants import *
from Player import *

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
sock.connect(('localhost', 10000))

pygame.init()
screen = pygame.display.set_mode((WIDTH_ROOM, HEIGHT_ROOM))
pygame.display.set_caption('Игра')


def draw_characters():
    pass


def draw_rects(s):
    rects = s.split(',')
    for rect in rects:
        if rect != '':
            a = rect.split(' ')
            cords = (int(a[0]),
                     int(a[1]),
                     int(a[2]),
                     int(a[3]))
            pygame.draw.rect(screen, (255, 0, 0), cords)


def draw_arches(s):
    arches = s.split(',')
    for arch in arches:
        if arch != '':
            a = arch.split(' ')
            x = int(a[0])
            y = int(a[1])
            direction = int(a[2])
            image = pygame.image.load('templates/arch_up.png').convert_alpha()
            if direction == 0:
                x += 18
                y -= 20
            if direction == 1:
                image = pygame.image.load('templates/arch_right.png').convert_alpha()
                x += 25
                y += 22
            elif direction == 2:
                image = pygame.image.load('templates/arch_down.png').convert_alpha()
                x += 18
                y += 25
            elif direction == 3:
                image = pygame.image.load('templates/arch_left.png').convert_alpha()
                x -= 20
                y += 22
            screen.blit(image, (x, y))


def draw_players(s):
    players = s.split(',')
    for player in players:
        if player != ('' or ' '):
            a = player.split(' ')
            x = int(a[0])
            y = int(a[1])
            direction = int(a[2])
            hp = int(a[3])
            hp_width = 45 * hp / 100
            images = [pygame.image.load('templates/archer_up.png').convert_alpha(),
                      pygame.image.load('templates/archer_right.png').convert_alpha(),
                      pygame.image.load('templates/archer_down.png').convert_alpha(),
                      pygame.image.load('templates/archer_left.png').convert_alpha(),
                      pygame.image.load('templates/archer_kill.png').convert_alpha(),
                      pygame.image.load('templates/archer_up_atack.png').convert_alpha(),
                      pygame.image.load('templates/archer_right_atack.png').convert_alpha(),
                      pygame.image.load('templates/archer_down_atack.png').convert_alpha(),
                      pygame.image.load('templates/archer_left_atack.png').convert_alpha()]
            if hp <= 0:
                direction = 4
            pygame.draw.rect(screen, (255, 0, 0), (x, y + 45, 45, 5))
            pygame.draw.rect(screen, (0, 255, 0), (x, y + 45, hp_width, 5))
            screen.blit(images[direction], (x, y))


def draw_bonuses(s):
    bonuses = s.split(',')
    for bonus in bonuses:
        if bonus != '':
            a = bonus.split(' ')
            x = int(a[0])
            y = int(a[1])
            color = color_bonuses[int(a[2])]
            pygame.draw.rect(screen, color, (x, y, 20, 20))


def draw_menu(s):
    menus = s.split(',')
    for menu in menus:
        if menu != '':
            a = menu.split(' ')
            atack_tick = int(a[0])
            q_tick = int(a[1])

            num_atack = (3 - atack_tick * (3/180))
            text1 = str(num_atack)[:3]
            if num_atack > 0:
                f1 = pygame.font.Font(None, 50)
                text1 = f1.render(text1, True, (255, 255, 255))
                screen.blit(text1, (WIDTH_ROOM - 170, HEIGHT_ROOM - 370))

            num_q = (5 - q_tick * (5 / 300))
            text2 = str(num_q)[:3]
            if num_q > 0:
                f2 = pygame.font.Font(None, 50)
                text1 = f2.render(text2, True, (255, 255, 255))
                screen.blit(text1, (WIDTH_ROOM - 170, HEIGHT_ROOM - 270))


def draw_bots(s):
    bots = s.split(',')
    for bot in bots:
        if bot != '':
            a = bot.split(' ')
            x = int(a[0])
            y = int(a[1])
            direction = int(a[2])
            hp = int(a[3])
            hp_width = 45 * hp / 100
            images = [pygame.image.load('templates/archer_up.png').convert_alpha(),
                      pygame.image.load('templates/archer_right.png').convert_alpha(),
                      pygame.image.load('templates/archer_down.png').convert_alpha(),
                      pygame.image.load('templates/archer_left.png').convert_alpha(),
                      pygame.image.load('templates/archer_kill.png').convert_alpha(),
                      pygame.image.load('templates/archer_up_atack.png').convert_alpha(),
                      pygame.image.load('templates/archer_right_atack.png').convert_alpha(),
                      pygame.image.load('templates/archer_down_atack.png').convert_alpha(),
                      pygame.image.load('templates/archer_left_atack.png').convert_alpha()]
            pygame.draw.rect(screen, (255, 0, 0), (x, y + 45, 45, 5))
            pygame.draw.rect(screen, (0, 255, 0), (x, y + 45, hp_width, 5))
            screen.blit(images[direction], (x, y))


def find_rects(s):
    first = None
    for i in range(len(s)):
        if s[i] == '<':
            first = i + 1
        if s[i] == '/' and first is not None:
            last = i
            res = s[first:last]
            return res
    return ''


def find(s):
    first = None
    for i in range(len(s)):
        if s[i] == '/':
            first = i + 1
        if s[i] == '|' and first is not None:
            last = i
            res = s[first:last]
            return res
    return ''


def find_arches(s):
    first = None
    for i in range(len(s)):
        if s[i] == '|':
            first = i + 1
        if s[i] == '!' and first is not None:
            last = i
            res = s[first:last]
            return res
    return ''


def find_bonuses(s):
    first = None
    for i in range(len(s)):
        if s[i] == '!':
            first = i + 1
        if s[i] == '&' and first is not None:
            last = i
            res = s[first:last]
            return res
    return ''


def find_menu(s):
    first = None
    for i in range(len(s)):
        if s[i] == '&':
            first = i + 1
        if s[i] == '%' and first is not None:
            last = i
            res = s[first:last]
            return res
    return ''


def find_bots(s):
    first = None
    for i in range(len(s)):
        if s[i] == '%':
            first = i + 1
        if s[i] == '>' and first is not None:
            last = i
            res = s[first:last]
            return res
    return ''


motion = 'STOP'
running = True
while running:
    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                motion = 'LEFT'
            elif event.key == pygame.K_d:
                motion = 'RIGHT'
            elif event.key == pygame.K_w:
                motion = 'UP'
            elif event.key == pygame.K_s:
                motion = 'DOWN'
            elif event.key == pygame.K_SPACE:
                motion = 'SPACE'
            elif event.key == pygame.K_q:
                motion = 'Q'
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_SPACE, pygame.K_q]:
                motion = 'STOP'

    # отправляем инфу серверу
    sock.send(motion.encode())

    # получаем от сервера новое состояние игры
    data = sock.recv(1024).decode()
    data_rects = find_rects(data)
    data_players = find(data)
    data_arches = find_arches(data)
    data_bonuses = find_bonuses(data)
    data_menu = find_menu(data)
    data_bots = find_bots(data)

    # рисуем новое состояние игрового поля
    screen.fill('gray25')
    pygame.draw.rect(screen, (0, 0, 0), (WIDTH_ROOM - WIDTH_MENU, 0, WIDTH_MENU, HEIGHT_ROOM))
    draw_rects(data_rects)
    draw_bonuses(data_bonuses)
    draw_players(data_players)
    draw_arches(data_arches)
    draw_menu(data_menu)
    draw_bots(data_bots)

    pygame.display.update()
pygame.quit()