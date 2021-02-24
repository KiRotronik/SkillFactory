import random


class BoardException(Exception):
    pass


class BoardOutException(BoardException):
    def __str__(self):
        return "You shoot outside the board"


class BoardUsedException(BoardException):
    def __str__(self):
        return "You've already shot this cage"

class BoardWrongShipException(BoardException):
    pass


class Ship:
    def __init__(self, bow, l, dir):
        self.l = l
        self.bow = bow
        self.dir = dir
        self.life = l
    @property
    def dots(self):
        ship_dots = []
        for i in range(self.l):
            cur_x = self.bow.x
            cur_y = self.bow.y

            if self.dir == 0:
                cur_x += i

            elif self.dir == 1:
                cur_y += i
            ship_dots.append(Dot(cur_x, cur_y))

        return ship_dots

    def shooten(self, shot):
        return shot in self.dots


class Board:
    def __init__(self, hid=False, size=6):
        self.size = size
        self.hid = hid

        self.count = 0
        self.field = [['O']* self.size for _ in range(self.size)]
        self.ships =[]
        self.busy = []

    def __str__(self):
        res = "    1   2   3   4   5   6  "
        for i, row in enumerate(self.field):
            res += f"\n {i+1} + row"

    def add_ship(self):
    def contour(self):
    def visible(self):
        if not hid:


    def out(self, d):
        return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))
    
    def shot(self, x, y):
        self.x = x
        self.y = y
        try:



class Player:
    def move():
        a, b = User.ask()
        Board.shot(a, b)
        return a, b


class User(Player):
    @staticmethod
    def ask():
        while True:
            cords = input("Enter x,y coordinates for shoot").split()
            if len(cords) != 2:
                print("Enter two digits from 1 to 6")
                continue
            x, y = cords
            if not x.isdigit() and y.isdigit():
                print("Enter two digits from 1 to 6")
                continue
            x, y = int(x), int(y)
            if x < 1 or x > 6 and y < 1 or y > 6:
                print("Enter two digits from 1 to 6")
                continue
            else:
                return x, y


class Ai:
    def ask():
        x, y = random.randint(1, 6), random.randint(1, 6)
        return x, y


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Dot{self.x}, {self.y}"

class Game:
    def welcome(self):
        print("---------------")
        print("--- Welcome ---")
        print("----- to ------")
        print("- SEA BATTLE --")
        print("---- GAME! ----")
        print("---------------")

    def random_board(self):

    def greet(self):
    def loop(self):
    def start(self):

d = Dot()
print(d)