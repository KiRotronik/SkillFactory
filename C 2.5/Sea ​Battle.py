class Board:
    def create_board(self):
        print("    1   2   3   4   5   6  ")
        for i in range(6):
            row = (['| O' for j in range(6)])
            print( i + 1, *row )



class Ship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Ship_1(Ship):

class Dot:



compB = Board()
playerB = Board()
f.create_board()
f.create_board()


