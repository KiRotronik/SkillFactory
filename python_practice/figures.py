class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    def get_area(self):
        return self.height * self.width

class Square:
    def __init__(self, a):
        self.a = a
    def get_area_square(self):
        return self.a ** 2

class Circle:
    def __init__(self, r):
        self.r = r
    def get_area_circle(self):
        return 3,14159 * self.r ** 2