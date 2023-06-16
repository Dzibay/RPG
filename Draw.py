import pygame
from Constants import *

screen = pygame.display.set_mode((WIDTH_ROOM, HEIGHT_ROOM))

menu = [(350, 275, 300, 50)]

items_icons = [{1: pygame.image.load('templates/items/damage_1.png'),
                2: pygame.image.load('templates/items/damage_2.png'),
                3: pygame.image.load('templates/items/damage_3.png')},

               {1: pygame.image.load('templates/items/armor_1.png'),
                2: pygame.image.load('templates/items/armor_2.png'),
                3: pygame.image.load('templates/items/armor_3.png')},

               {1: pygame.image.load('templates/items/atack_speed_1.png'),
                2: pygame.image.load('templates/items/atack_speed_2.png'),
                3: pygame.image.load('templates/items/atack_speed_3.png')},

               {1: pygame.image.load('templates/items/damage_1.png'),
                2: pygame.image.load('templates/items/damage_2.png'),
                3: pygame.image.load('templates/items/damage_3.png')}]

menu_items_cords = [(WIDTH_ROOM - 185, 180), (WIDTH_ROOM - 95, 180),
                    (WIDTH_ROOM - 185, 290), (WIDTH_ROOM - 95, 290)]


def draw_item_effect(screen, item, player):
    if item == 'linkens_sphere':
        pygame.draw.circle(screen, (255, 255, 255), (player.x + 22, player.y + 22), 22)


def draw_item_ticks(screen, tick, place):
    if tick > 0:
        num = str(tick / 60)[:4]
        f1 = pygame.font.Font(None, 50)
        text1 = f1.render(num, True, (255, 255, 255))
        screen.blit(text1, (menu_items_cords[place][0] + 11, menu_items_cords[place][1] + 20))


def draw_menu(screen):
    f1 = pygame.font.Font(None, 50)
    pygame.draw.rect(screen, (0, 200, 0), menu[0])
    text1 = f1.render('Start Game', True, (255, 255, 255))
    screen.blit(text1, (400, 282))


def draw_doors(screen, doors):
    for door in doors:
        if door != ():
            pygame.draw.rect(screen, (0, 255, 0), door)


def draw_play_menu(screen, items, gold):
    f1 = pygame.font.Font(None, 30)
    for i in range(len(menu_items_cords)):
        can = (100, 100, 100)
        screen.blit(items_icons[i][items[i]], menu_items_cords[i])
        if gold >= items[i] * 1000:
            can = (200, 200, 0)
        pygame.draw.rect(screen, can, (menu_items_cords[i][0], menu_items_cords[i][1] + 66, 80, 30))
        if items[i] < 3:
            text = f1.render(str(items[i] * 1000), True, (255, 255, 255))
            screen.blit(text, (menu_items_cords[i][0] + 20, menu_items_cords[i][1] + 72))

        pygame.draw.rect(screen, (255, 255, 255), (menu_items_cords[i][0], menu_items_cords[i][1], 80, 96), 1)
        pygame.draw.rect(screen, (255, 255, 255), (menu_items_cords[i][0], menu_items_cords[i][1] + 66, 80, 1))

    f2 = pygame.font.Font(None, 40)
    text_gold = f2.render(str(gold), True, (255, 255, 255))
    screen.blit(text_gold, (WIDTH_ROOM - 175, HEIGHT_ROOM - 115))
    pygame.draw.rect(screen, (0, 200, 0), (850, 540, 100, 50))


arches_img = [pygame.image.load('templates/archer/arch_up.png').convert_alpha(),
              pygame.image.load('templates/archer/arch_right.png').convert_alpha(),
              pygame.image.load('templates/archer/arch_down.png').convert_alpha(),
              pygame.image.load('templates/archer/arch_left.png').convert_alpha()]


def draw_arches(screen, arches):
    for arch in arches:
        x = int(arch[0])
        y = int(arch[1])
        direction = int(arch[2])
        image = arches_img[direction]
        if direction == 0:
            x += 18
            y -= 20
        if direction == 1:
            x += 25
            y += 22
        elif direction == 2:
            x += 18
            y += 25
        elif direction == 3:
            x -= 20
            y += 22
        screen.blit(image, (x, y))


player_img = [pygame.image.load('templates/archer/archer_up.png').convert_alpha(),  # 0
              pygame.image.load('templates/archer/archer_right.png').convert_alpha(),  # 1
              pygame.image.load('templates/archer/archer_down.png').convert_alpha(),  # 2
              pygame.image.load('templates/archer/archer_left.png').convert_alpha(),  # 3
              pygame.image.load('templates/archer/archer_kill.png').convert_alpha(),  # 4

              pygame.image.load('templates/archer/archer_up_atack.png').convert_alpha(),  # 5
              pygame.image.load('templates/archer/archer_right_atack.png').convert_alpha(),  # 6
              pygame.image.load('templates/archer/archer_down_atack.png').convert_alpha(),  # 7
              pygame.image.load('templates/archer/archer_left_atack.png').convert_alpha(),  # 8

              pygame.image.load('templates/archer/archer_up_atack_1.png').convert_alpha(),  # 9
              pygame.image.load('templates/archer/archer_right_atack_1.png').convert_alpha(),  # 10
              pygame.image.load('templates/archer/archer_down_atack_1.png').convert_alpha(),  # 11
              pygame.image.load('templates/archer/archer_left_atack_1.png').convert_alpha()]


def draw_player(screen, player):
    hp_width = 45 * player.hp / 100

    pygame.draw.rect(screen, (255, 0, 0), (player.x, player.y + 45, 45, 5))
    pygame.draw.rect(screen, (0, 255, 0), (player.x, player.y + 45, hp_width, 5))
    screen.blit(player_img[player.direction], (player.x, player.y))


enemy_img = {'mini_orc': [pygame.image.load('templates/mini_orc/mini_orc_up.png').convert_alpha(),  # 0
                          pygame.image.load('templates/mini_orc/mini_orc_right.png').convert_alpha(),  # 1
                          pygame.image.load('templates/mini_orc/mini_orc_down.png').convert_alpha(),  # 2
                          pygame.image.load('templates/mini_orc/mini_orc_left.png').convert_alpha(),  # 3
                          pygame.image.load('templates/mini_orc/mini_orc_kill.png').convert_alpha(),  # 4

                          pygame.image.load('templates/mini_orc/mini_orc_up_atack.png').convert_alpha(),  # 5
                          pygame.image.load('templates/mini_orc/mini_orc_up_atack_1.png').convert_alpha(),  # 6
                          pygame.image.load('templates/mini_orc/mini_orc_up_atack_2.png').convert_alpha(),  # 7
                          pygame.image.load('templates/mini_orc/mini_orc_up_atack_3.png').convert_alpha(),  # 8

                          pygame.image.load('templates/mini_orc/mini_orc_right_atack.png').convert_alpha(),  # 9
                          pygame.image.load('templates/mini_orc/mini_orc_right_atack_1.png').convert_alpha(),  # 10
                          pygame.image.load('templates/mini_orc/mini_orc_right_atack_2.png').convert_alpha(),  # 11
                          pygame.image.load('templates/mini_orc/mini_orc_right_atack_3.png').convert_alpha(),  # 12

                          pygame.image.load('templates/mini_orc/mini_orc_down_atack.png').convert_alpha(),  # 13
                          pygame.image.load('templates/mini_orc/mini_orc_down_atack_1.png').convert_alpha(),  # 14
                          pygame.image.load('templates/mini_orc/mini_orc_down_atack_2.png').convert_alpha(),  # 15
                          pygame.image.load('templates/mini_orc/mini_orc_down_atack_3.png').convert_alpha(),  # 16

                          pygame.image.load('templates/mini_orc/mini_orc_left_atack.png').convert_alpha(),  # 17
                          pygame.image.load('templates/mini_orc/mini_orc_left_atack_1.png').convert_alpha(),  # 18
                          pygame.image.load('templates/mini_orc/mini_orc_left_atack_2.png').convert_alpha(),  # 19
                          pygame.image.load('templates/mini_orc/mini_orc_left_atack_3.png').convert_alpha(),  # 20

                          pygame.image.load('templates/mini_orc/mini_orc_up_1.png').convert_alpha(),  # 21
                          pygame.image.load('templates/mini_orc/mini_orc_up_2.png').convert_alpha(),  # 22
                          pygame.image.load('templates/mini_orc/mini_orc_right_1.png').convert_alpha(),  # 23
                          pygame.image.load('templates/mini_orc/mini_orc_right_2.png').convert_alpha(),  # 24
                          pygame.image.load('templates/mini_orc/mini_orc_down_1.png').convert_alpha(),  # 25
                          pygame.image.load('templates/mini_orc/mini_orc_down_2.png').convert_alpha(),  # 26
                          pygame.image.load('templates/mini_orc/mini_orc_left_1.png').convert_alpha(),  # 27
                          pygame.image.load('templates/mini_orc/mini_orc_left_2.png').convert_alpha()],  # 28

             'orc': [pygame.image.load('templates/orc/orc_up.png').convert_alpha(),  # 0
                     pygame.image.load('templates/orc/orc_right.png').convert_alpha(),  # 1
                     pygame.image.load('templates/orc/orc_down.png').convert_alpha(),  # 2
                     pygame.image.load('templates/orc/orc_left.png').convert_alpha(),  # 3
                     pygame.image.load('templates/orc/orc_kill.png').convert_alpha(),  # 4

                     pygame.image.load('templates/orc/orc_up_atack.png').convert_alpha(),  # 5
                     pygame.image.load('templates/orc/orc_up_atack_1.png').convert_alpha(),  # 6
                     pygame.image.load('templates/orc/orc_up_atack_2.png').convert_alpha(),  # 7
                     pygame.image.load('templates/orc/orc_up_atack_3.png').convert_alpha(),  # 8

                     pygame.image.load('templates/orc/orc_right_atack.png').convert_alpha(),  # 9
                     pygame.image.load('templates/orc/orc_right_atack_1.png').convert_alpha(),  # 10
                     pygame.image.load('templates/orc/orc_right_atack_2.png').convert_alpha(),  # 11
                     pygame.image.load('templates/orc/orc_right_atack_3.png').convert_alpha(),  # 12

                     pygame.image.load('templates/orc/orc_down_atack.png').convert_alpha(),  # 13
                     pygame.image.load('templates/orc/orc_down_atack_1.png').convert_alpha(),  # 14
                     pygame.image.load('templates/orc/orc_down_atack_2.png').convert_alpha(),  # 15
                     pygame.image.load('templates/orc/orc_down_atack_3.png').convert_alpha(),  # 16

                     pygame.image.load('templates/orc/orc_left_atack.png').convert_alpha(),  # 17
                     pygame.image.load('templates/orc/orc_left_atack_1.png').convert_alpha(),  # 18
                     pygame.image.load('templates/orc/orc_left_atack_2.png').convert_alpha(),  # 19
                     pygame.image.load('templates/orc/orc_left_atack_3.png').convert_alpha(),  # 20

                     pygame.image.load('templates/orc/orc_up_1.png').convert_alpha(),  # 21
                     pygame.image.load('templates/orc/orc_up_2.png').convert_alpha(),  # 22
                     pygame.image.load('templates/orc/orc_right_1.png').convert_alpha(),  # 23
                     pygame.image.load('templates/orc/orc_right_2.png').convert_alpha(),  # 24
                     pygame.image.load('templates/orc/orc_down_1.png').convert_alpha(),  # 25
                     pygame.image.load('templates/orc/orc_down_2.png').convert_alpha(),  # 26
                     pygame.image.load('templates/orc/orc_left_1.png').convert_alpha(),  # 27
                     pygame.image.load('templates/orc/orc_left_2.png').convert_alpha()],  # 28
             'mega_orc': [pygame.image.load('templates/mega_orc/mega_orc_up.png').convert_alpha(),  # 0
                          pygame.image.load('templates/mega_orc/mega_orc_right.png').convert_alpha(),  # 1
                          pygame.image.load('templates/mega_orc/mega_orc_down.png').convert_alpha(),  # 2
                          pygame.image.load('templates/mega_orc/mega_orc_left.png').convert_alpha(),  # 3
                          pygame.image.load('templates/troll/troll_kill.png').convert_alpha(),  # 4

                          pygame.image.load('templates/mega_orc/mega_orc_up_atack.png').convert_alpha(),  # 5
                          pygame.image.load('templates/mega_orc/mega_orc_up_atack_1.png').convert_alpha(),  # 6
                          pygame.image.load('templates/mega_orc/mega_orc_up_atack_2.png').convert_alpha(),  # 7
                          pygame.image.load('templates/mega_orc/mega_orc_up_atack_3.png').convert_alpha(),  # 8

                          pygame.image.load('templates/mega_orc/mega_orc_right_atack.png').convert_alpha(),  # 9
                          pygame.image.load('templates/mega_orc/mega_orc_right_atack_1.png').convert_alpha(),  # 10
                          pygame.image.load('templates/mega_orc/mega_orc_right_atack_2.png').convert_alpha(),  # 11
                          pygame.image.load('templates/mega_orc/mega_orc_right_atack_3.png').convert_alpha(),  # 12

                          pygame.image.load('templates/mega_orc/mega_orc_down_atack.png').convert_alpha(),  # 13
                          pygame.image.load('templates/mega_orc/mega_orc_down_atack_1.png').convert_alpha(),  # 14
                          pygame.image.load('templates/mega_orc/mega_orc_down_atack_2.png').convert_alpha(),  # 15
                          pygame.image.load('templates/mega_orc/mega_orc_down_atack_3.png').convert_alpha(),  # 16

                          pygame.image.load('templates/mega_orc/mega_orc_left_atack.png').convert_alpha(),  # 17
                          pygame.image.load('templates/mega_orc/mega_orc_left_atack_1.png').convert_alpha(),  # 18
                          pygame.image.load('templates/mega_orc/mega_orc_left_atack_2.png').convert_alpha(),  # 19
                          pygame.image.load('templates/mega_orc/mega_orc_left_atack_3.png').convert_alpha(),  # 20

                          pygame.image.load('templates/mega_orc/mega_orc_up_1.png').convert_alpha(),  # 21
                          pygame.image.load('templates/mega_orc/mega_orc_up_2.png').convert_alpha(),  # 22
                          pygame.image.load('templates/mega_orc/mega_orc_right_1.png').convert_alpha(),  # 23
                          pygame.image.load('templates/mega_orc/mega_orc_right_2.png').convert_alpha(),  # 24
                          pygame.image.load('templates/mega_orc/mega_orc_down_1.png').convert_alpha(),  # 25
                          pygame.image.load('templates/mega_orc/mega_orc_down_2.png').convert_alpha(),  # 26
                          pygame.image.load('templates/mega_orc/mega_orc_left_1.png').convert_alpha(),  # 27
                          pygame.image.load('templates/mega_orc/mega_orc_left_2.png').convert_alpha()],  # 28
             'troll': [pygame.image.load('templates/troll/troll_up.png').convert_alpha(),  # 0
                       pygame.image.load('templates/troll/troll_right.png').convert_alpha(),  # 1
                       pygame.image.load('templates/troll/troll_down.png').convert_alpha(),  # 2
                       pygame.image.load('templates/troll/troll_left.png').convert_alpha(),  # 3
                       pygame.image.load('templates/troll/troll_kill.png').convert_alpha(),  # 4

                       pygame.image.load('templates/troll/troll_up_atack.png').convert_alpha(),  # 5
                       pygame.image.load('templates/troll/troll_up_atack_1.png').convert_alpha(),  # 6
                       pygame.image.load('templates/troll/troll_up_atack_2.png').convert_alpha(),  # 7
                       pygame.image.load('templates/troll/troll_up_atack_3.png').convert_alpha(),  # 8

                       pygame.image.load('templates/troll/troll_right_atack.png').convert_alpha(),  # 9
                       pygame.image.load('templates/troll/troll_right_atack_1.png').convert_alpha(),  # 10
                       pygame.image.load('templates/troll/troll_right_atack_2.png').convert_alpha(),  # 11
                       pygame.image.load('templates/troll/troll_right_atack_3.png').convert_alpha(),  # 12

                       pygame.image.load('templates/troll/troll_down_atack.png').convert_alpha(),  # 13
                       pygame.image.load('templates/troll/troll_down_atack_1.png').convert_alpha(),  # 14
                       pygame.image.load('templates/troll/troll_down_atack_2.png').convert_alpha(),  # 15
                       pygame.image.load('templates/troll/troll_down_atack_3.png').convert_alpha(),  # 16

                       pygame.image.load('templates/troll/troll_left_atack.png').convert_alpha(),  # 17
                       pygame.image.load('templates/troll/troll_left_atack_1.png').convert_alpha(),  # 18
                       pygame.image.load('templates/troll/troll_left_atack_2.png').convert_alpha(),  # 19
                       pygame.image.load('templates/troll/troll_left_atack_3.png').convert_alpha(),  # 20

                       pygame.image.load('templates/troll/troll_up_1.png').convert_alpha(),  # 21
                       pygame.image.load('templates/troll/troll_up_2.png').convert_alpha(),  # 22
                       pygame.image.load('templates/troll/troll_right_1.png').convert_alpha(),  # 23
                       pygame.image.load('templates/troll/troll_right_2.png').convert_alpha(),  # 24
                       pygame.image.load('templates/troll/troll_down_1.png').convert_alpha(),  # 25
                       pygame.image.load('templates/troll/troll_down_2.png').convert_alpha(),  # 26
                       pygame.image.load('templates/troll/troll_left_1.png').convert_alpha(),  # 27
                       pygame.image.load('templates/troll/troll_left_2.png').convert_alpha()],  # 28
             'people_ship': [pygame.image.load('templates/people_ship/people_ship_up.png').convert_alpha(),  # 0
                             pygame.image.load('templates/people_ship/people_ship_right.png').convert_alpha(),  # 1
                             pygame.image.load('templates/people_ship/people_ship_down.png').convert_alpha(),  # 2
                             pygame.image.load('templates/people_ship/people_ship_left.png').convert_alpha(),  # 3
                             pygame.image.load('templates/people_ship/people_ship_kill.png').convert_alpha(),  # 4
                             pygame.image.load('templates/people_ship/people_ship_kill_1.png').convert_alpha(),  # 5
                             pygame.image.load('templates/people_ship/people_ship_right_up.png').convert_alpha()],  # 6
             'jagernault': [pygame.image.load('templates/jagernault/jagernault_up.png').convert_alpha(),  # 0
                            pygame.image.load('templates/jagernault/jagernault_right.png').convert_alpha(),  # 1
                            pygame.image.load('templates/jagernault/jagernault_down.png').convert_alpha(),  # 2
                            pygame.image.load('templates/jagernault/jagernault_left.png').convert_alpha(),  # 3
                            pygame.image.load('templates/jagernault/jagernault_kill.png').convert_alpha(),  # 4
                            pygame.image.load('templates/jagernault/jagernault_right_up.png').convert_alpha(),  # 5
                            pygame.image.load('templates/jagernault/jagernault_kill_1.png').convert_alpha()],  # 6
             'ballist': [pygame.image.load('templates/ballist/ballist_left_up.png').convert_alpha(),  # 0
                         pygame.image.load('templates/ballist/ballist_left_up_atack.png').convert_alpha(),  # 1
                         pygame.image.load('templates/ballist/ballist_left_up_atack_1.png').convert_alpha()],  # 2
             'catapult': [pygame.image.load('templates/catapult/catapult_down.png').convert_alpha(),  # 0
                          pygame.image.load('templates/catapult/catapult_down_atack.png').convert_alpha(),  # 1
                          pygame.image.load('templates/catapult/catapult_down_atack_1.png').convert_alpha()]}  # 2


def draw_enemy(screen, bot, enemy=True):
    hp_width = 0
    max_hp_width = 0
    images = enemy_img[bot.type]
    if bot.type == 'mini_orc':
        hp_width = (bot.size + 10) * bot.hp / 100
        max_hp_width = bot.size + 10
    elif bot.type == 'orc':
        hp_width = 45 * bot.hp / 100
        max_hp_width = 45
    elif bot.type == 'mega_orc':
        hp_width = (bot.size + 10) * bot.hp / 100
        max_hp_width = bot.size + 10
    elif bot.type == 'troll':
        hp_width = (bot.size + 10) * bot.hp / 100
        max_hp_width = bot.size + 10
    if enemy:
        pygame.draw.rect(screen, (255, 0, 0), (bot.x, bot.y + bot.size, max_hp_width, 5))
        pygame.draw.rect(screen, (0, 255, 0), (bot.x, bot.y + bot.size, hp_width, 5))
    screen.blit(images[bot.direction], (bot.x, bot.y))
