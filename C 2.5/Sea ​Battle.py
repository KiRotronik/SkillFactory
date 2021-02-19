import random


class BoardOutException:
    pass

class Board:
    hid =
    def create_board(self,):
        print("    1   2   3   4   5   6  ")
        for i in range(6):
            row = (['| O' for j in range(6)])
            print( i + 1, *row )
    def add_ship(self):
    def contour(self):
    def visible(self):
    def out(self):
    def shot(self):



class Ship:
    def __init__(self, leight, x, y, dir, life):
        self.leight = leight
        self.x = x
        self.y = y
        self.dir = dir
        self.life = life
    def dots(self):
        return

class User(Player):
    def ask(self):
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
    def move(self, x, y):
        x, y = self.ask()

class Ai(Player):
    def ask(self):
        x, y = random.randint(0,6), random.randint(0,6)
        return x, y

class User(Player):
    def ask(self):
        x, y = input("Enter x,y coordinates for shoot").split()
        if not x.isdigit() and y.isdigit():
            print("Enter two digit from 1 to 6")
        if x < 1 or x > 6 and y < 1 or y > 6:
            print("Enter two digit from 1 to 6")
        else:
            return x, y



class Dot:
    dots = [[O for j in range(6)]for i in range(6)]
    def coord(self, x, y):
        self.cord = dots[y][x]

    def __eq__(self, other):

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