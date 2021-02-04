class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def str_rec(self):
        return f"Rectangle ({self.x}, {self.y}, {self.width}, {self.height})"

rec_1 = Rectangle(5, 10, 50, 100)
print(rec_1.str_rec())