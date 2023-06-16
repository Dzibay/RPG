import random
import pygame
from random import randint
from Constants import *
from Player import *
from Draw import *
from dextr import *
import copy

pygame.init()

clock = pygame.time.Clock()


def get_rects(file):
    res = []
    file = open(file, 'r').readlines()
    file = [i.replace('\n', '') for i in file]
    for y in range(len(file)):
        for x in range(len(file[0])):
            if file[y][x] == '1':
                res.append((x * 50, y * 50, 50, 50))
    return res


def get_water(file):
    water = []
    file = open(file, 'r').readlines()
    file = [i.replace('\n', '') for i in file]
    for y in range(len(file)):
        for x in range(len(file[0])):
            if file[y][x] == '2':
                water.append((x * 50, y * 50, 50, 50))
    return water


level_1 = Level([Orc(200, 100)],
                get_rects('levels/lvl1.txt'), get_water('levels/lvl1.txt'),
                [(100, 0, 450, 10), (), (), ()],
                pygame.image.load('levels/texture/lvl1.png'), 'levels/lvl1.txt', {})
level_2 = Level([Orc(300, 0), Orc(600, 100), Mini_orc(200, 400)],
                get_rects('levels/lvl2.txt'), get_water('levels/lvl2.txt'),
                [(250, 0, 400, 10), (), (100, 590, 450, 10), ()],
                pygame.image.load('levels/texture/lvl2.png'), 'levels/lvl2.txt', {})
level_3 = Level([Mega_orc(600, 50), Mega_orc(700, 200)],
                get_rects('levels/lvl3.txt'), get_water('levels/lvl3.txt'),
                [(450, 0, 350, 10), (790, 0, 10, 400), (250, 590, 400, 10), ()],
                pygame.image.load('levels/texture/lvl3.png'), 'levels/lvl3.txt',
                {Orc(60, 250): [[0, 0, 100, 0, 0, 200, 0, 200, 100], [0, 0, 100, 0, 0, 200, 0, 200, 100]],
                 Orc(220, 200): [[200, 0, 200, 0], [200, 0, 200, 0]]})
level_4 = Level([Troll(740, 0), Orc(600, 200), Mini_orc(500, 50), Mini_orc(40, 60)],
                get_rects('levels/lvl4.txt'), get_water('levels/lvl4.txt'),
                [(), (790, 0, 10, 300), (), (0, 0, 10, 400)],
                pygame.image.load('levels/texture/lvl4.png'), 'levels/lvl4.txt', {})
level_5 = Level([Troll(740, 500), Troll(700, 350), Troll(700, 20)],
                get_rects('levels/lvl5.txt'), get_water('levels/lvl5.txt'),
                [(), (), (410, 590, 390, 10), (0, 0, 10, 300)],
                pygame.image.load('levels/texture/lvl5.png'), 'levels/lvl5.txt', {})
level_6 = Level([Mega_orc(500, 520), Troll(720, 400)],
                get_rects('levels/lvl6.txt'), get_water('levels/lvl6.txt'),
                [(410, 0, 390, 10), (), (510, 590, 290, 10), ()],
                pygame.image.load('levels/texture/lvl6.png'), 'levels/lvl6.txt', {})
level_7 = Level([Troll(40, 500), Troll(200, 450), Mega_orc(720, 550), Orc(400, 300)],
                get_rects('levels/lvl7.txt'), get_water('levels/lvl7.txt'),
                [(510, 0, 290, 10), (), (), (0, 350, 10, 300)],
                pygame.image.load('levels/texture/lvl7.png'), 'levels/lvl7.txt', {})
level_8 = Level([],
                get_rects('levels/lvl8.txt'), get_water('levels/lvl8.txt'),
                [(), (790, 350, 10, 300), (), ()],
                pygame.image.load('levels/texture/lvl8.png'), 'levels/lvl8.txt', {},
                (Jagernault(-200, 500), People_ship(-115, 450)))
level_10 = Level([],
                 get_rects('levels/lvl10.txt'), get_water('levels/lvl10.txt'),
                 [(), (), (450, 595, 350, 10), ()],
                 pygame.image.load('levels/texture/lvl10.png'), 'levels/lvl10.txt', {},
                 ((), Ballist(800, 600), Catapult(730, -65)))

level_bots = {1: level_1.bots, 2: level_2.bots, 3: level_3.bots, 4: level_4.bots, 5: level_5.bots,
              6: level_6.bots, 7: level_7.bots, 8: level_8.bots, 10: level_10.bots}
level_rects = {1: level_1.rects, 2: level_2.rects, 3: level_3.rects, 4: level_4.rects, 5: level_5.rects,
               6: level_6.rects, 7: level_7.rects, 8: level_8.rects, 10: level_10.rects}
level_water = {1: level_1.water, 2: level_2.water, 3: level_3.water, 4: level_4.water, 5: level_5.water,
               6: level_6.water, 7: level_7.water, 8: level_8.water, 10: level_10.water}
level_doors = {1: level_1.doors, 2: level_2.doors, 3: level_3.doors, 4: level_4.doors, 5: level_5.doors,
               6: level_6.doors, 7: level_7.doors, 8: level_8.doors, 10: level_10.doors}
level_files = {1: level_1.lvl_file, 2: level_2.lvl_file, 3: level_3.lvl_file, 4: level_4.lvl_file, 5: level_5.lvl_file,
               6: level_6.lvl_file, 7: level_7.lvl_file, 8: level_8.lvl_file, 10: level_10.doors}
level_bg = {1: level_1.bg, 2: level_2.bg, 3: level_3.bg, 4: level_4.bg, 5: level_5.bg,
            6: level_6.bg, 7: level_7.bg, 8: level_8.bg, 10: level_10.bg}
level_static_bots = {1: level_1.static_bots, 2: level_2.static_bots, 3: level_3.static_bots, 4: level_4.static_bots,
                     5: level_5.static_bots, 6: level_6.static_bots, 7: level_7.static_bots, 8: level_8.static_bots}

jagernault_bullet = pygame.image.load('templates/jagernault/bullet.png')
ballist_bullet = pygame.image.load('templates/ballist/bullet.png')

menu_bg = pygame.image.load('levels/texture/menu.png')
change_lvl = False
lvl_file = 'menu.txt'
motion = 'STOP'
level = 'menu'
arches = []
items = []
bots = []
room_rects = []
doors = []
arch_tick = 0
play_tick = 0
level_8_tick = 0
level_10_tick = 0
item_sell_id = None
shop = Shop(130, 250)


def hp_box(x, y, size_x, size_y):
    res = [(i, j)
           for i in range(x - HP_BOX_DIF, x + size_x - HP_BOX_DIF)
           for j in range(y - HP_BOX_DIF, y + size_y - HP_BOX_DIF)]
    return res


def move_room_check(gamer, can):
    if gamer.y <= 0 + player.speed:
        can[0] = 1
        if motion == 'UP':
            gamer.y = 1
    if gamer.x + gamer.size >= WIDTH_ROOM - WIDTH_MENU - player.speed:
        can[1] = 1
        if motion == 'LEFT':
            gamer.x = WIDTH_ROOM - WIDTH_MENU - gamer.size - 1
    if gamer.y + gamer.size >= HEIGHT_ROOM - player.speed:
        can[2] = 1
        if motion == 'DOWN':
            gamer.y = HEIGHT_ROOM - gamer.size - 1
    if gamer.x <= 0 + player.speed:
        can[3] = 1
        if motion == 'RIGHT':
            gamer.x = 1
    return can


def move_check(gamer, obj, can):
    if (gamer.y <= obj[1] + obj[3] + SIZE_DIF) and \
            (gamer.x < obj[0] + obj[2]) and \
            (gamer.x + gamer.size > obj[0]) and \
            (gamer.y > obj[1]):
        can[0] = 1
    if (gamer.x + gamer.size >= obj[0] - SIZE_DIF) and \
            (gamer.y < obj[1] + obj[3]) and \
            (gamer.y + gamer.size > obj[1]) and \
            (gamer.x < obj[0] + obj[2]):
        can[1] = 1
    if (gamer.y + gamer.size >= obj[1] - SIZE_DIF) and \
            (gamer.x < obj[0] + obj[2]) and \
            (gamer.x + gamer.size > obj[0]) and \
            (gamer.y < obj[1] + obj[3]):
        can[2] = 1
    if (gamer.x <= obj[0] + obj[2] + SIZE_DIF) and \
            (gamer.y < obj[1] + obj[3]) and \
            (gamer.y + gamer.size > obj[1]) and \
            (gamer.x > obj[0]):
        can[3] = 1
    return can


def move(data):
    if play_tick % 2 == 0:
        if data == 'UP':
            player.direction = 0
            player.last_direction = 0
            if player.can[0] == 0:
                return [0, -1]
        elif data == 'LEFT':
            player.direction = 3
            player.last_direction = 3
            if player.can[3] == 0:
                return [-1, 0]
        elif data == 'DOWN':
            player.direction = 2
            player.last_direction = 2
            if player.can[2] == 0:
                return [0, 1]
        elif data == 'RIGHT':
            player.direction = 1
            player.last_direction = 1
            if player.can[1] == 0:
                return [1, 0]
    return [0, 0]


def add_arches():
    if player.direction == 0:
        arches.append([player.x, player.y, player.direction, 'y-'])
    if player.direction == 1:
        arches.append([player.x, player.y, player.direction, 'x+'])
    if player.direction == 2:
        arches.append([player.x, player.y, player.direction, 'y+'])
    if player.direction == 3:
        arches.append([player.x, player.y, player.direction, 'x-'])


def arches_events():
    for arch in arches:
        if arch[2] == 0:
            arch[1] -= ARCH_SPEED
            arch_cords = (arch[0], arch[1] - 25)
        elif arch[2] == 1:
            arch[0] += ARCH_SPEED
            arch_cords = (arch[0] + 25, arch[1])
        elif arch[2] == 2:
            arch[1] += ARCH_SPEED
            arch_cords = (arch[0], arch[1] + 25)
        else:
            arch[0] -= ARCH_SPEED
            arch_cords = (arch[0] - 25, arch[1])

        # попадание стрелы в моба
        for bot in bots:
            if arch_cords in hp_box(bot.x, bot.y, bot.size, bot.size):
                arches.remove(arch)
                bot.hp -= player.damage * (1 - bot.armor / 100)

                # отбрасываем ботов
                if arch[3] == 'x+':
                    bot.x += player.reclining
                if arch[3] == 'x-':
                    bot.x -= player.reclining
                if arch[3] == 'y+':
                    bot.y += player.reclining
                if arch[3] == 'y-':
                    bot.y -= player.reclining

        # попадание в стену
        for rect in room_rects:
            if arch_cords in hp_box(rect[0], rect[1], rect[2], rect[3]):
                arches.remove(arch)
        if arch[0] > WIDTH_ROOM - (WIDTH_MENU + 40) or arch[1] > HEIGHT_ROOM or arch[0] < -10 or arch[1] < -10:
            arches.remove(arch)


def move_bots():
    for bot in bots:
        # выбор направления для бота
        bot_cords = (get_cords((bot.x, bot.y)))
        player_cords = (get_cords((player.x, player.y)))

        if bot.direction in [0, 21, 22]:
            bot_cords = (get_cords((bot.x, bot.y + bot.size)))
        elif bot.direction in [3, 27, 28]:
            bot_cords = (get_cords((bot.x + bot.size, bot.y)))

        print(bot_cords, player_cords)
        bot.direction = get_direction(bot_cords, player_cords, lvl_file, bot.direction)

        # убийство бота
        if bot.hp <= 0:
            bot.direction = 4
            bot.kill_tick += 1
            if bot.kill_tick == 30:
                player.gold += bot.award
                bots.remove(bot)

        # само передвижение бота
        bot_moving(bot)


def bot_moving(bot):
    if play_tick % 2 == 0:
        if (bot.direction in [0, 21, 22]) and bot.can[0] == 0:
            bot.y -= bot.speed
            bot.going += 1
        elif (bot.direction in [1, 23, 24]) and bot.can[1] == 0:
            bot.x += bot.speed
            bot.going += 1
        elif (bot.direction in [2, 25, 26]) and bot.can[2] == 0:
            bot.y += bot.speed
            bot.going += 1
        elif (bot.direction in [3, 27, 28]) and bot.can[3] == 0:
            bot.x -= bot.speed
            bot.going += 1
    else:
        bot.stoping += 1
        if bot.stoping > 60:
            bot.stoping_2 += 1
    if bot.can == [0, 0, 0, 0]:
        bot.stoping = 0
        bot.stoping_2 = 0

    # делаем анимацию движения
    if (bot.going <= 10) and (bot.going > 0):
        if bot.direction in [0, 22]:
            bot.direction = 21
        if bot.direction in [1, 24]:
            bot.direction = 23
        if bot.direction in [2, 26]:
            bot.direction = 25
        if bot.direction in [3, 28]:
            bot.direction = 27
    elif bot.going > 10:
        if bot.direction in [0, 21]:
            bot.direction = 22
        if bot.direction in [1, 23]:
            bot.direction = 24
        if bot.direction in [2, 25]:
            bot.direction = 26
        if bot.direction in [3, 27]:
            bot.direction = 28
    if bot.going == 20:
        bot.going = 0


def bot_fight(bot, player):
    dist_x = abs(player.x - bot.x)
    dist_y = abs(player.y - bot.y)
    if bot.atack_tick == bot.atack_speed and \
            dist_x <= 45 + SIZE_DIF and \
            dist_y <= 45 + SIZE_DIF:
        bot.atack_tick = 0
    if bot.atack_tick < bot.atack_speed:
        bot.atack_tick += 1
    if bot.atack_tick < bot.atack_speed // 18:
        if bot.direction in [0, 21, 22]:
            bot.direction = 5
        elif bot.direction in [1, 23, 24]:
            bot.direction = 9
        elif bot.direction in [2, 25, 26]:
            bot.direction = 13
        elif bot.direction in [3, 27, 28]:
            bot.direction = 17
    elif bot.atack_tick < bot.atack_speed // 12:
        if bot.direction in [0, 21, 22]:
            bot.direction = 6
        elif bot.direction in [1, 23, 24]:
            bot.direction = 10
        elif bot.direction in [2, 25, 26]:
            bot.direction = 14
        elif bot.direction in [3, 27, 28]:
            bot.direction = 18
    elif bot.atack_tick < bot.atack_speed // 9:
        if bot.direction in [0, 21, 22]:
            bot.direction = 7
        elif bot.direction in [1, 23, 24]:
            bot.direction = 11
        elif bot.direction in [2, 25, 26]:
            bot.direction = 15
        elif bot.direction in [3, 27, 28]:
            bot.direction = 19
    elif bot.atack_tick == bot.atack_speed // 8:
        armor = player.armor
        if armor > 100:
            armor = 100
        player.hp -= bot.damage * (1 - armor / 100)
        if bot.recling > 0:
            if bot.direction in [0, 21, 22]:
                player.y -= bot.recling
                if player.y < 0:
                    player.y = 1
            elif bot.direction in [1, 23, 24]:
                player.x += bot.recling
                if player.x + player.size > WIDTH_ROOM - WIDTH_MENU:
                    player.x = WIDTH_ROOM - WIDTH_MENU - player.size - 1
            elif bot.direction in [2, 25, 26]:
                player.y += bot.recling
                if player.y + player.size > HEIGHT_ROOM:
                    player.y = HEIGHT_ROOM - player.size - 1
            elif bot.direction in [3, 27, 28]:
                player.x -= bot.recling
                if player.x < 0:
                    player.x = 1
        player.is_stunned = bot.stun
    elif bot.atack_tick < bot.atack_speed // 4.5:
        if bot.direction in [0, 21, 22]:
            bot.direction = 8
        elif bot.direction in [1, 23, 24]:
            bot.direction = 12
        elif bot.direction in [2, 25, 26]:
            bot.direction = 16
        elif bot.direction in [3, 27, 28]:
            bot.direction = 20


def jagernault_atack(boss, bullet):
    for i in boss.atack:
        if (i[0] + 10 > player.x) and (i[0] + 10 < player.x + player.size) and (i[1] + 5 > player.y) and (i[1] + 5 < player.y + player.size):
            boss.atack.remove(i)
            player.hp -= boss.damage * (1 - player.armor / 100)
        elif i[0] > 800:
            boss.atack.remove(i)
        elif i[2] == 1:
            i[0] += 4
        elif i[2] == 5:
            i[0] += 2
            i[1] -= 2
        screen.blit(bullet, (i[0], i[1]))


def level_8_boss():
    boss = level_8.boss[0]
    people_ship = level_8.boss[1]
    jagernault_atack(boss, jagernault_bullet)
    if level_8_tick <= 1200:
        if play_tick % 2 == 0:
            if level_8_tick < 500:
                people_ship.direction = 1
                people_ship.x += 1
                boss.direction = 1
                boss.x += 1
            elif level_8_tick < 800:
                people_ship.direction = 6
                people_ship.x += 1
                people_ship.y -= 1
        if level_8_tick == 600:
            boss.direction = 5
        elif level_8_tick == 700:
            boss.atack.append([boss.x + 80, boss.y + 20, boss.direction])
        elif level_8_tick == 800:
            boss.atack = []
            people_ship.direction = 4
    else:
        if boss.hp > 0:
            boss.atack_tick += 1
            if boss.y + 35 < player.y + 5:
                boss.direction = 2
                boss.y += 1
            elif boss.y + 50 > player.y + player.size - 5:
                boss.direction = 0
                boss.y -= 1
            else:
                boss.direction = 1
                if boss.atack_tick > boss.atack_speed:
                    boss.atack.append([boss.x + 90, boss.y + 40, 1])
                    boss.atack_tick = 0
        else:
            boss.direction = 4
            boss.kill_tick += 1
            if boss.kill_tick > 100:
                boss.direction = 6
    for arch in arches:
        if (arch[0] - 40 < boss.x) and (arch[1] > boss.y) and (arch[1] < boss.y + 95):
            boss.hp -= player.damage * (1 - boss.armor / 100)
            arches.remove(arch)
    if level_8_tick > 1000:
        people_ship.direction = 5

    if boss.hp > 0:
        pygame.draw.rect(screen, (255, 0, 0), (boss.x - 6, boss.y + 100, 100, 5))
        pygame.draw.rect(screen, (0, 255, 0), (boss.x - 6, boss.y + 100, boss.hp, 5))
    draw_enemy(screen, people_ship)
    draw_enemy(screen, boss)


def ballist_atack(ballist, bullet):
    ballist.atack_tick += 1
    for i in ballist.atack:
        if i[1] < 80:
            ballist.atack.remove(i)
        elif i[2] == 5:
            i[0] -= 5
            i[1] -= 5
        screen.blit(bullet, (i[0], i[1]))


def level_10_boss():
    ballist = level_10.boss[1]
    catapult_down = level_10.boss[2]
    ballist_atack(ballist, ballist_bullet)
    if level_10_tick < 150:
        if play_tick % 2 == 0:
            ballist.x -= 1
            ballist.y -= 1
    elif (level_10_tick > 200) and (level_10_tick < 301):
        if level_10_tick < 220:
            ballist.direction = 1
        elif level_10_tick == 220:
            ballist.atack.append([ballist.x - 30, ballist.y - 30, 5])
        elif level_10_tick < 240:
            ballist.direction = 2
        elif level_10_tick > 300:
            ballist.direction = 0
    elif (level_10_tick > 400) and (level_10_tick < 800):
        if play_tick % 2 == 0:
            catapult_down.y += 1

    elif level_10_tick > 800:
        pygame.draw.rect(screen, (255, 0, 0), (catapult_down.x, catapult_down.y + 65, 65, 5))
        pygame.draw.rect(screen, (0, 255, 0), (catapult_down.x, catapult_down.y + 65, 65 * catapult_down.hp / 100, 5))

        if ballist.atack_tick >= ballist.atack_speed + 20:
            ballist.direction = 1
            ballist.atack_tick = 0
        elif ballist.atack_tick == 10:
            ballist.atack.append([ballist.x - 30, ballist.y - 30, 5])
            ballist.direction = 2
        elif ballist.atack_tick == ballist.atack_speed:
            ballist.direction = 0

    for arch in arches:
        if (arch[0] > catapult_down.x) and (arch[0] < catapult_down.x + 65) and (arch[1] < catapult_down.y + 65):
            arches.remove(arch)
            catapult_down.hp -= player.damage - (1 - catapult_down.armor / 100)
    draw_enemy(screen, ballist)
    draw_enemy(screen, catapult_down)


def player_atack_animation():
    if player.atack_tick < 5:
        if player.direction in [0, 5]:
            player.direction = 5
        if player.direction in [1, 6]:
            player.direction = 6
        if player.direction in [2, 7]:
            player.direction = 7
        if player.direction in [3, 8]:
            player.direction = 8
    elif player.atack_tick < player.atack_speed:
        if player.direction in [0, 5, 9]:
            player.direction = 9
        if player.direction in [1, 6, 10]:
            player.direction = 10
        if player.direction in [2, 7, 11]:
            player.direction = 11
        if player.direction in [3, 8, 12]:
            player.direction = 12
    else:
        if player.direction in [0, 5, 9]:
            player.direction = 0
        if player.direction in [1, 6, 10]:
            player.direction = 1
        if player.direction in [2, 7, 11]:
            player.direction = 2
        if player.direction in [3, 8, 12]:
            player.direction = 3


def in_box(cords, box):
    res = False
    if cords[0] > box[0]:
        if cords[0] < box[0] + box[2]:
            if cords[1] > box[1]:
                if cords[1] < box[1] + box[3]:
                    res = True
    return res


def next_level(motion, door):
    if motion == 'UP':
        if (player.x > door[0]) and (player.x + player.size < door[0] + door[2]) and \
                (player.y < door[1] + door[3]):
            return True
    elif motion == 'RIGHT':
        if (player.y > door[1]) and (player.y + player.size < door[1] + door[3]) and \
                (player.x + player.size > door[0]):
            return True
    elif motion == 'DOWN':
        if (player.x > door[0]) and (player.x + player.size < door[0] + door[2]) and \
                (player.y + player.size > door[1] - door[3]):
            return True
    elif motion == 'LEFT':
        if (player.y > door[1]) and (player.y + player.size < door[1] + door[3]) and \
                (player.x < door[0] + door[2]):
            return True


level_to_level = [{}, {'UP': 2},  # 1
                  {'UP': 3, 'DOWN': 1},  # 2
                  {'UP': 10, 'RIGHT': 4, 'DOWN': 2},  # 3
                  {'RIGHT': 5, 'LEFT': 3},  # 4
                  {'DOWN': 6, 'LEFT': 4},  # 5
                  {'UP': 5, 'DOWN': 7},  # 6
                  {'UP': 6, 'LEFT': 8},  # 7
                  {'RIGHT': 7},  # 8
                  {},
                  {'DOWN': 3}]  # 10


def changing_level(level, change_lvl):
    for i in level_to_level[level]:
        if i == 'UP':
            if next_level('UP', doors[0]):
                level = level_to_level[level][i]
                player.y = 540
                change_lvl = True
        elif i == 'LEFT':
            if next_level('LEFT', doors[3]):
                level = level_to_level[level][i]
                player.x = 740
                change_lvl = True
        elif i == 'DOWN':
            if next_level('DOWN', doors[2]):
                level = level_to_level[level][i]
                player.y = 10
                change_lvl = True
        elif i == 'RIGHT':
            if next_level('RIGHT', doors[1]):
                level = level_to_level[level][i]
                player.x = 10
                change_lvl = True

    return change_lvl, level


running = True
while running:
    clock.tick(FPS)
    pygame.display.set_caption(str(clock.get_fps()))
    if level == 'menu':
        bots = []
        room_rects = []
        room_water = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                start = menu[0]
                if (pos[0] > start[0]) and \
                        (pos[0] < start[0] + start[2]) and \
                        (pos[1] > start[1]) and \
                        (pos[1] < start[1] + start[3]):
                    level = START_LEVEL
                    player = Player(530, 375)
                    room_rects = level_rects[level]
                    room_water = level_water[level]
                    doors = level_doors[level]
                    bots = level_bots[level]
                    lvl_file = level_files[level]
        screen.blit(menu_bg, (0, 0))
        draw_menu(screen)
    else:
        # обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                motion = 'mouse_press'
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
                elif event.key == pygame.K_TAB:
                    motion = 'TAB'
                elif event.key == pygame.K_1:
                    motion = '1'
                elif event.key == pygame.K_2:
                    motion = '2'
                elif event.key == pygame.K_3:
                    motion = '3'
                elif event.key == pygame.K_4:
                    motion = '4'
                elif event.key == pygame.K_5:
                    motion = '5'
                elif event.key == pygame.K_6:
                    motion = '6'
            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_SPACE, pygame.K_TAB,
                                 pygame.K_1]:
                    motion = 'STOP'

        # проверяем игрока на стан
        if player.is_stunned > 0 or player.direction == 4:
            motion = 'STOP'

        # проверяем кому куда можно ходить
        for rect in room_rects:
            player.can = move_check(player, rect, player.can)  # игрок и стенки
        for wat in room_water:
            player.can = move_check(player, wat, player.can)  # игрок и вода
        player.can = move_room_check(player, player.can)  # игрок и границы
        for bot in bots:
            for rect in room_rects:
                bot.can = move_check(bot, rect, bot.can)  # бот и стенки

            bot.can = move_check(bot, [player.x, player.y, player.size, player.size], bot.can)  # бот и игрок
            player.can = move_check(player, [bot.x, bot.y, bot.size, bot.size], player.can)  # игрок и боты
            bot.can = move_room_check(bot, bot.can)  # бот и границы
            for bot1 in bots:
                if bot != bot1:
                    bot.can = move_check(bot, [bot1.x, bot1.y, bot1.size, bot1.size], bot.can)  # бот и боты

        move_bots()  # двигаем ботов

        # добавляем атаку ботам
        for bot in bots:
            if bot.direction != 4:
                bot_fight(bot, player)

        # добавляем стрелы
        if motion == 'SPACE' and player.atack_tick >= player.atack_speed:
            player.atack_tick = 0
            add_arches()
        else:
            for i in range(player.speed):
                player.x += move(motion)[0]
                player.y += move(motion)[1]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # передвижение стрел
        arches_events()

        # анимация атаки игрока
        player_atack_animation()

        # улучшение предметов
        if motion == 'mouse_press':
            pos = pygame.mouse.get_pos()
            if pos in hp_box(850, 540, 100, 50):
                if (player.gold >= 100) and (player.hp < 100):
                    player.gold -= 100
                    if player.hp <= 80:
                        player.hp += 20
                    else:
                        player.hp = 100
            for i in range(len(menu_items_cords)):
                if player.items[i] < 3:
                    if pos in hp_box(menu_items_cords[i][0], menu_items_cords[i][1], 80, 120):
                        if player.gold >= player.items[i] * 1000:
                            player.gold -= player.items[i] * 1000
                            player.items[i] += 1
                            if i == 0:
                                player.damage += 15
                            elif i == 1:
                                player.armor += 20
                            elif i == 2:
                                player.atack_speed -= 20
                            elif i == 3:
                                player.speed += 1
            motion = 'STOP'

        # обновляем возможность ходить у всех
        player.can = [0, 0, 0, 0]
        for bot in bots:
            bot.can = [0, 0, 0, 0]

        # дальность магазина
        if abs(player.x - shop.x) < shop.r and abs(player.y - shop.y) < shop.r:
            shop.can_buy = True
        else:
            shop.can_buy = False

        # тики
        play_tick += 1
        if player.is_stunned > 0:
            player.is_stunned -= 1
        if player.hp <= 0:
            player.kill_tick -= 1
            player.direction = 4
        if player.atack_tick < player.atack_speed:
            player.atack_tick += 1
        if player.kill_tick == 0:
            level = 'menu'

        # переход в другой уровень
        change_lvl, level = changing_level(level, change_lvl)
        if change_lvl:
            room_rects = level_rects[level]
            room_water = level_water[level]
            doors = level_doors[level]
            bots = level_bots[level]
            lvl_file = level_files[level]
            change_lvl = False

        # рисуем экран
        screen.blit(level_bg[level], (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), (WIDTH_ROOM - WIDTH_MENU, 0, WIDTH_MENU, HEIGHT_ROOM))

        draw_doors(screen, doors)
        draw_arches(screen, arches)
        draw_play_menu(screen, player.items, player.gold)
        for bot in bots:
            draw_enemy(screen, bot)

        draw_player(screen, player)

        if STATIC_BOT:
            for bot in level_static_bots[level]:
                directions = level_static_bots[level][bot][0]
                bot.direction = 0
                while True:
                    if directions[bot.direction] > 0:
                        break
                    else:
                        bot.direction += 1
                        if bot.direction == len(directions):
                            level_static_bots[level][bot][0] = copy.copy(level_static_bots[level][bot][1])
                            bot.direction = 0
                            break
                if bot.direction in [0, 4, 8, 12, 16]:
                    directions[bot.direction] -= 1
                    bot.direction = 0
                elif bot.direction in [1, 5, 9, 13, 17]:
                    directions[bot.direction] -= 1
                    bot.direction = 1
                elif bot.direction in [2, 6, 10, 14, 18]:
                    directions[bot.direction] -= 1
                    bot.direction = 2
                elif bot.direction in [3, 7, 11, 15, 19]:
                    directions[bot.direction] -= 1
                    bot.direction = 3
                bot_moving(bot)
                if bot.type == 'orc':
                    draw_enemy(screen, bot, False)
        if level == 8:
            level_8_tick += 1
            level_8_boss()
        elif level == 10:
            level_10_tick += 1
            level_10_boss()

    pygame.display.update()
pygame.quit()
