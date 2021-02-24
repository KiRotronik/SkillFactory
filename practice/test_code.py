class Board:
    def __init__(self, hid=False, size=6):
        self.size = size
        self.hid = hid

        self.count = 0
        self.field = [['O']* self.size for i in range(self.size)]
        self.ships =[]
        self.busy = []

    def __str__(self):
        res = "     1   2   3   4   5   6  "
        for i, row in enumerate(self.field):
            res += f"\n {i+1} | " + " | ".join(row) + " |"

        if self.hid:
            res = res.replace("■", "0")

        return res

b = Board()
print(b)