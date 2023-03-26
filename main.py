import pygame
import socket
from random import randint
from Constants import *
from Player import *

main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
main_socket.bind(('localhost', 10000))
main_socket.setblocking(0)
main_socket.listen(5)


pygame.init()
screen = pygame.display.set_mode((WIDTH_SERVER_ROOM, HEIGHT_SERVER_ROOM))
pygame.display.set_caption('Сервер')
clock = pygame.time.Clock()

# отправляем состояние комнаты
room_rects = []
message_room = ''
for rect in room_rects:
    message_room += str(rect[0]) + ' ' + str(rect[1]) + ' ' + str(rect[2]) + ' ' + str(rect[3]) + ','

room_server_rects = [(i[0] // 2, i[1] // 2, i[2] // 2, i[3] // 2) for i in room_rects]


def hp_box(x, y):
    res = [(i, j) for i in range(x-25, x+25) for j in range(y-25, y+25)]
    return res


def move_check(gamer, obj, can):
    if (gamer.y <= obj.y + gamer.size) and \
            (gamer.x <= obj.x + obj.size + SIZE_DIF) and \
            (gamer.x >= obj.x - obj.size+SIZE_DIF) and \
            (gamer.y >= obj.y):
        can[0] = 1
    if (gamer.x >= obj.x - gamer.size) and \
            (gamer.y <= obj.y + obj.size + SIZE_DIF) and \
            (gamer.y >= obj.y - obj.size + SIZE_DIF) and \
            (gamer.x <= obj.x + obj.size - SIZE_DIF):
        can[1] = 1
    if (gamer.y >= obj.y - gamer.size) and \
            (gamer.x <= obj.x + obj.size + SIZE_DIF) and \
            (gamer.x >= obj.x - obj.size + SIZE_DIF) and \
            (gamer.y <= obj.y):
        can[2] = 1
    if (gamer.x <= obj.x + gamer.size) and \
            (gamer.y <= obj.y + obj.size + SIZE_DIF) and \
            (gamer.y >= obj.y - obj.size + SIZE_DIF) and \
            (gamer.x >= obj.x + obj.size - SIZE_DIF):
        can[3] = 1

    if gamer.y < 0:
        can[0] = 1
    if gamer.x > WIDTH_ROOM - 50 - WIDTH_MENU:
        can[1] = 1
    if gamer.y > HEIGHT_ROOM - 50:
        can[2] = 1
    if gamer.x < 0:
        can[3] = 1
    return can


def draw_arches(x, y, direction):
    if direction == 0 or direction == 2:
        a, b = 5, 2
    else:
        a, b = 2, 5
    if direction == 0:
        pygame.draw.rect(screen, (255, 0, 0), (x // 2 + 11, y // 2 - a, a, b))
    elif direction == 1:
        pygame.draw.rect(screen, (255, 0, 0), (x // 2 + 22, y //2 + 11, a, b))
    elif direction == 2:
        pygame.draw.rect(screen, (255, 0, 0), (x // 2 + 9, y // 2 + 22, a, b))
    elif direction == 3:
        pygame.draw.rect(screen, (255, 0, 0), (x // 2 - a, y // 2 + 11, a, b))


def move(data, speed):
    if data == 'LEFT' and player.can[3] == 0:
        player.direction = 3
        return [-speed, 0]
    elif data == 'RIGHT' and player.can[1] == 0:
        player.direction = 1
        return [speed, 0]
    elif data == 'UP' and player.can[0] == 0:
        player.direction = 0
        return [0, -speed]
    elif data == 'DOWN' and player.can[2] == 0:
        player.direction = 2
        return [0, speed]
    else:
        return [0, 0]


def q_move():
    if player.direction == 0:
        player.y -= Q_MOVE
        for bot in bots:
            player.can = move_check(player, bot, player.can)
        for player1 in players:
            if player != player1:
                player.can = move_check(player, player1, player.can)
        if player.can[0] == 0:
            player.y -= Q_MOVE
            player.q_tick = 0
        player.y += Q_MOVE

    if player.direction == 1:
        player.x += Q_MOVE
        for bot in bots:
            player.can = move_check(player, bot, player.can)
        for player1 in players:
            if player != player1:
                player.can = move_check(player, player1, player.can)
        if player.can[1] == 0:
            player.x += Q_MOVE
            player.q_tick = 0
        player.x -= Q_MOVE

    if player.direction == 2:
        player.y += Q_MOVE
        for bot in bots:
            player.can = move_check(player, bot, player.can)
        for player1 in players:
            if player != player1:
                player.can = move_check(player, player1, player.can)
        if player.can[2] == 0:
            player.y += Q_MOVE
            player.q_tick = 0
        player.y -= Q_MOVE

    if player.direction == 3:
        player.x -= Q_MOVE
        for bot in bots:
            player.can = move_check(player, bot, player.can)
        for player1 in players:
            if player != player1:
                player.can = move_check(player, player1, player.can)
        if player.can[3] == 0:
            player.x -= Q_MOVE
            player.q_tick = 0
        player.x += Q_MOVE


def message():
    sms = '<'

    # стены
    sms += message_room
    sms += '/'

    # игроки
    for player in players:
        if player.atack_direction == 20:
            player.direction = player.last_direction
        sms = sms + str(player.x) + ' ' + str(player.y) + ' ' + str(player.direction) + ' ' + str(player.hp) + ','
    sms += ' |'

    # стрелы
    for i in arches:
        sms += str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[2]) + ','
    sms += '!'

    # бонусы
    for bonus in bonuses:
        sms += str(bonus[0]) + ' ' + str(bonus[1]) + ' ' + str(bonus[2]) + ','
    sms += '&'

    # тики способностей
    sms += str(c.atack_tick) + ' ' + str(c.q_tick) + ','
    sms += '%'

    # боты
    for bot in bots:
        sms += str(bot.x) + ' ' + str(bot.y) + ' ' + str(bot.direction) + ' ' + str(bot.hp) + ','
    sms += '>'

    return sms


print('Сервер создан')
arches = []
players = []
bonuses = []
bots = []
arch_tick = 0
bonus_tick = 0
id = 0
server_work = True
while server_work:
    clock.tick(FPS)
    if len(bonuses) < MAX_BONUSES_IN_ROOM:
        bonus_tick += 1

    # проверяем, есть ли желающие присоединится к игре
    try:
        new_socket, addr = main_socket.accept()
        print('Подключился', addr)
        new_socket.setblocking(0)
        new_player = Player(new_socket, addr, WIDTH_ROOM // 2, HEIGHT_ROOM // 2, id)
        players.append(new_player)
        id += 1
    except:
        pass

    # добавляем ботов
    if len(bots) < MAX_BOTS_QUANTITY:
        new_bot = Bot(randint(100, WIDTH_ROOM - WIDTH_MENU - 100), randint(100, HEIGHT_ROOM - 100))
        bots.append(new_bot)

    # проверяем кому куда можно ходить
    for player in players:
        for bot in bots:
            bot.can = move_check(bot, player, bot.can)
            player.can = move_check(player, bot, player.can)
        for player1 in players:
            if player != player1:
                player.can = move_check(player, player1, player.can)
    for bot in bots:
        for bot1 in bots:
            if bot != bot1:
                bot.can = move_check(bot, bot1, bot.can)

    # двигаем ботов
    for bot in bots:
        if bot.hp <= 0:
            bots.remove(bot)
        else:
            if (bot.direction == 0) and bot.can[0] == 0:
                bot.y -= bot.speed
            if (bot.direction == 1) and bot.can[1] == 0:
                bot.x += bot.speed
            if (bot.direction == 2) and bot.can[2] == 0:
                bot.y += bot.speed
            if (bot.direction == 3) and bot.can[3] == 0:
                bot.x -= bot.speed

            if bot.move_tick > 200:
                a = randint(0, 3)
                bot.direction = a
                bot.move_tick = 0
            bot.move_tick += 1

    # добавляем бонусы
    if len(bonuses) < MAX_BONUSES_IN_ROOM and bonus_tick > BONUS__SPAWN_TICK:
        bonuses.append([randint(50, WIDTH_ROOM - WIDTH_MENU - 50),
                        randint(50, HEIGHT_ROOM - WIDTH_MENU - 50),
                        randint(1, 4)])
        bonus_tick = 0

    # считываем команды игроков
    for player in players:
        player.q_tick += 1

        # проверяем взяли ли игроки бонусы
        if player.bonus_quantity < MAX_BONUS_PLAYER_QUANTITY:
            for bonus in bonuses:
                if (bonus[0], bonus[1]) in hp_box(player.x, player.y):
                    bonuses.remove(bonus)
                    bonus_tick = 0
                    player.bonus_quantity += 1
                    if bonus[2] == 1:
                        player.hp += BONUS_HP
                    elif bonus[2] == 2:
                        player.damage += BONUS_DAMAGE
                    elif bonus[2] == 3:
                        player.reclining += BONUS_RECLING
                    elif bonus[2] == 4:
                        player.reclining += BONUS_SPEED
        player.atack_tick += 1
        player.atack_direction += 1
        if player.hp <= 0:
            player.connection.close()
        try:
            data = player.connection.recv(1024).decode()

            # добавляем стрелы
            if data == 'SPACE' and player.atack_tick > player.atack_speed:

                # добавляем стреле отбрасывание
                r_ = player.reclining
                if player.direction == 0:
                    arches.append([player.x, player.y, player.direction, player.id, player.damage, 'y-', r_])
                if player.direction == 1:
                    arches.append([player.x, player.y, player.direction, player.id, player.damage, 'x+', r_])
                if player.direction == 2:
                    arches.append([player.x, player.y, player.direction, player.id, player.damage, 'y+', r_])
                if player.direction == 3:
                    arches.append([player.x, player.y, player.direction, player.id, player.damage, 'x-', r_])

                player.atack_tick = 0
                player.atack_direction = 0
                player.last_direction = player.direction
                if player.direction == 0:
                    player.direction = 5
                elif player.direction == 1:
                    player.direction = 6
                elif player.direction == 2:
                    player.direction = 7
                elif player.direction == 3:
                    player.direction = 8

            # проверка нажатия Q
            elif data == 'Q':
                if player.q_tick > player.q_speed:
                    q_move()

            else:
                player.x += move(data, player.speed)[0]
                player.y += move(data, player.speed)[1]
        except:
            pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            server_work = False

    # ответ каждому игроку:
    for c in players:
        sms = message()

        # отравляем новое состояние игрового поля
        try:
            c.connection.send(sms.encode())
            errors = 0
        except:
            c.errors += 1

    # чистим список от отключившихся игроков
    for player in players:
        if player.errors == 500:
            player.connection.close()
            players.remove(player)
            print('Отключился игрок')

    # рисуем игроков
    screen.fill('gray25')
    for player in players:
        pygame.draw.circle(screen, (0, 255, 0),
                           (player.x // 2 + 10,
                            player.y // 2 + 10),
                           10)

    # рисуем ботов
    for bot in bots:
        pygame.draw.circle(screen, (255, 0, 0),
                           (bot.x // 2,
                            bot.y // 2),
                           10)

    # отрисовка стрел
    for arch in arches:
        draw_arches(arch[0], arch[1], arch[2])
        if arch[2] == 0:
            arch[1] -= ARCH_SPEED
        elif arch[2] == 1:
            arch[0] += ARCH_SPEED
        elif arch[2] == 2:
            arch[1] += ARCH_SPEED
        elif arch[2] == 3:
            arch[0] -= ARCH_SPEED

    # удаляем стрелы
    for arch in arches:

        # попадание в игрока
        for player in players:
            if (arch[0], arch[1]) in hp_box(player.x, player.y) and player.id != arch[3]:
                arches.remove(arch)

                # отбрасываем игроков
                player.hp -= arch[4]
                if arch[5] == 'x+':
                    player.x += arch[6]
                if arch[5] == 'x-':
                    player.x -= arch[6]
                if arch[5] == 'y+':
                    player.y += arch[6]
                if arch[5] == 'y-':
                    player.y -= arch[6]

        # попадание в моба
        for bot in bots:
            if (arch[0], arch[1]) in hp_box(bot.x, bot.y):
                arches.remove(arch)

                # отбрасываем ботов
                bot.hp -= arch[4]
                if arch[5] == 'x+':
                    bot.x += arch[6]
                if arch[5] == 'x-':
                    bot.x -= arch[6]
                if arch[5] == 'y+':
                    bot.y += arch[6]
                if arch[5] == 'y-':
                    bot.y -= arch[6]

        if arch[0] > WIDTH_ROOM - (WIDTH_MENU+40) or arch[1] > HEIGHT_ROOM or arch[0] < -10 or arch[1] < -10:
            arches.remove(arch)

    # рисуем комнату
    for rect in room_server_rects:
        pygame.draw.rect(screen, (255, 0, 0), rect)

    # рисуем бонусы
    for bonus in bonuses:
        pygame.draw.rect(screen, color_bonuses[bonus[2]], (bonus[0] // 2, bonus[1] // 2, 10, 10))

    # обновляем возможность ходить у всех
    for player in players:
        player.can = [0, 0, 0, 0]
    for bot in bots:
        bot.can = [0, 0, 0, 0]

    pygame.display.update()
print('Сервер завершил работу')
pygame.quit()
main_socket.close()
