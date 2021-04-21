from random import randint


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


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Dot({self.x}, {self.y})"


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
        res = "     1   2   3   4   5   6  "
        for i, row in enumerate(self.field):
            res += f"\n {i + 1} | " + " | ".join(row) + " |"

        if self.hid:
            res = res.replace("■", "0")

        return res


    def out(self, dot):
        return not ((0 <= dot.x < self.size) and (0 <= dot.y < self.size))


    def contour(self, ship, verb=False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for d in ship.dots:
            for dx, dy in near:
                cur = Dot(d.x + dx, d.y + dy)
                if not (self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.field[cur.x][cur.y] = '.'
                    self.busy.append(cur)

    def add_ship(self, ship):
        for d in ship.dots:
            if self.out(d) or d in self.busy:
                raise BoardWrongShipException()
        for d in ship.dots:
            self.field[d.x][d.y] = "■"
            self.busy.append(d)

        self.ships.append(ship)
        self.contour(ship)

    def shot(self, d):
        if self.out(d):
            raise BoardOutException()

        if d in self.busy:
            raise BoardUsedException()

        self.busy.append(d)

        for ship in self.ships:
            if ship.shooten(d):
                ship.lives -= 1
                self.field[d.x][d.y] = 'X'
                if ship.lives == 0:
                    self.count +=1
                    self.contour(ship,verb=True)
                    print("Ship destroyed!")
                    return False
                else:
                    print("Ship wounded!")
                    return True

        self.field[d.x][d.y] = '.'
        print("Miss!")
        return False

    def begin(self):
        self.busy = []


class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)


class User(Player):
    @staticmethod
    def ask():
        while True:
            cords = input("Enter x,y coordinates for shoot").split()
            if len(cords) != 2:
                print("Enter two coordinates")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                print("Enter digits")
                continue

            x, y = int(x), int(y)

            return Dot(x - 1, y - 1)


class Ai(Player):
    def ask(self):
        d = Dot(randint(0, 5), randint(0, 5)
        print(f"Ai move: {d.x + 1} {d.y + 1}")
        return d




class Game:
    def try_board(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size = self.size)
        attemps = 0
        for l in lens:
            while True:
                attemps += 1
                if attemps > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size), l, randint(0, 1)))
                try:
                    board.add_ship(ship)

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
