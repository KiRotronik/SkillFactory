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

class Player:
    def ask(self):
    def move(self):

class Ai(Player):
    def ask(self):
class User(Player):
    def ask(self):

class Dot:
    def coord(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):

class Game:
    def random_board(self):
    def greet(self):
    def loop(self):
    def start(self):


