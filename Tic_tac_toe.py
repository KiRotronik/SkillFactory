def startgreet():
    print('-----------------')
    print('-- Tik Tac Toe --')
    print('-----------------')

def show_field():
    print('    1   2   3')
    print('  -------------')
    for i in range(3):
        row = ' | '.join(field[i])
        print(i+1, '|', row, '|',)
        print('  -------------')

def enter_cords():
    while True:
        x, y = input('Enter the x and y coordinates separated by space:\n').split()
        if x.isdigit() and y.isdigit():
            if 0 < x < 4 and 0 < y < 4:
                if field[x][y] == ' ':
                    return x, y
                else:
                    print("Cell is occupied")
            else:
                print("Enter x and y greater than 0 and less than 4")
        else:
            print("Enter digits")

field = [[' ']*3 for i in range(3)]
field[1][2] = 'X'
enter_cords()

print(show_field())
