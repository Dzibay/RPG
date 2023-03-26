class Player:
    def __init__(self, connection, addr, x, y, id):
        self.connection = connection
        self.addr = addr
        self.x = x
        self.y = y
        self.id = id

        self.can = [0, 0, 0, 0]
        self.speed = 5
        self.hp = 100
        self.atack_speed = 180
        self.damage = 20
        self.bonus_quantity = 0

        self.size = 45
        self.errors = 0
        self.direction = 0
        self.last_direction = 0
        self.atack_direction = 0
        self.atack_tick = self.atack_speed
        self.reclining = 0

        self.q_speed = 300
        self.q_tick = self.q_speed


class Bot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.can = [0, 0, 0, 0]
        self.size = 45
        self.direction = 0
        self.speed = 2
        self.hp = 100
        self.atack_speed = 180
        self.damage = 20
        self.atack_tick = self.atack_speed
        self.recling = 0
        self.move_tick = 0

