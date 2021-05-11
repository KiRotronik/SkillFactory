
pi = 3.14

def circ_area(radius):
    return radius**2 * pi

def rec_area(side_1, side_2):
    return side_1 * side_2

if __name__ == '__main__':
   # проверяем работоспособность функции, дальнейшая часть не будет импортирована
   assert circ_area(5) == 78.5  # если ответы будут отличаться, то будет вызвана ошибка
   assert rec_area(5, 4) == 20