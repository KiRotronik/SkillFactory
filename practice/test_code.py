class SquareFactory:
    @staticmethod
    def side(a):
        return Square(a)

class Square:
    def __init__(self, sa):
        self.sname = sa

pp = SquareFactory.side('5')
print(pp.sname)

