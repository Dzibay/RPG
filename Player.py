class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.items = [1, 1, 1, 1]
        self.damage = 20
        self.armor = 20
        self.atack_speed = 120
        self.speed = 3

        self.hp = 100
        self.reclining = 0
        self.stun = 0

        self.can = [0, 0, 0, 0]
        self.size = 40
        self.errors = 0
        self.direction = 0
        self.last_direction = 0
        self.atack_tick = self.atack_speed
        self.is_stunned = 0
        self.kill_tick = 60
        self.gold = 10000


class Bot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.type = ''
        self.stoping = 0
        self.stoping_2 = 0
        self.going = 0
        self.kill_tick = 0
        self.can = [0, 0, 0, 0]
        self.size = 45
        self.direction = 0
        self.last_direction = 0
        self.atack_tick = 0
        self.move_tick = 0

        self.speed = 0
        self.hp = 100
        self.armor = 0
        self.atack_speed = 180
        self.damage = 0
        self.recling = 0
        self.stun = 0
        self.award = 0


class Mini_orc(Bot):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = 'mini_orc'
        self.size = 25

        self.speed = 1
        self.atack_speed = 120
        self.atack_tick = self.atack_speed
        self.armor = -100
        self.damage = 10
        self.award = 100


class Orc(Bot):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = 'orc'

        self.speed = 2
        self.atack_speed = 180
        self.atack_tick = self.atack_speed
        self.armor = 15
        self.damage = 20
        self.award = 200


class Mega_orc(Bot):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = 'mega_orc'

        self.speed = 3
        self.atack_speed = 180
        self.atack_tick = self.atack_speed
        self.armor = 30
        self.damage = 30
        self.award = 400


class Troll(Bot):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = 'troll'

        self.speed = 2
        self.atack_speed = 250
        self.atack_tick = self.atack_speed
        self.armor = 50
        self.damage = 60
        self.stun = 60
        self.award = 700


class People_ship(Bot):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = 'people_ship'

        self.speed = 2
        self.atack_speed = 250
        self.atack_tick = self.atack_speed
        self.armor = 95
        self.damage = 60
        self.award = 2000


class Jagernault(Bot):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = 'jagernault'

        self.speed = 1
        self.atack_speed = 60
        self.atack_tick = self.atack_speed
        self.armor = 95
        self.damage = 100
        self.award = 3000
        self.atack = []
        self.kill_tick = 0


class Ballist(Bot):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = 'ballist'

        self.atack_speed = 200
        self.atack_tick = 0
        self.damage = 100
        self.atack = []


class Catapult(Bot):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = 'catapult'

        self.atack_speed = 200
        self.atack_tick = 0
        self.damage = 100
        self.atack = []


class Level:
    def __init__(self, bots, rects, water, doors, bg, lvl_file, static_bots, boss=None):
        self.bots = bots
        self.rects = rects
        self.water = water
        self.doors = doors
        self.bg = bg
        self.lvl_file = lvl_file
        self.static_bots = static_bots
        self.boss = boss

        self.tick = 0


class Shop:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 1000

        self.items = ['boots', 'blades_of_atack', 'chainmail', 'hyperstone', 'healing_salve']
        self.open = False
        self.can_buy = False
