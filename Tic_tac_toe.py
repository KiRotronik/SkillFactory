def startgreet():
    print('-----------------')
    print('-- Tik Tac Toe --')
    print('-----------------')

field = [[' ']*3 for i in range(3)]


def show_field():
    print('    1   2   3')
    print('  -------------')
    for i in range(3):
        row = ' | '.join(field[i])
        print(i+1, '|', row, '|',)
        print('  -------------')

def move():
    x, y = map(int, input('Your move, \nplease enter the x and y coordinates separated by space:\n').split())
    return x, y

x, y = move()
show_field()
print(field[x][y])