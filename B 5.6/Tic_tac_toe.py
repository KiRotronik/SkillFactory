def startgreet():
    print('-----------------')
    print('-- Tik Tac Toe --')
    print('-----------------')
    print('Enter the x and y\n-- coordinates --\n--- separated ---\n--- by space! ---')
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
        cords = input().split()
        if len(cords) != 2:
            print("Enter two digits")
            continue
        x, y = cords
        if not(x.isdigit()) or not(y.isdigit()):
            print("Enter digits")
            continue
        x, y = int(x), int(y)
        if 1 > x or x > 3 or 1 > y or y > 3:
            print("Enter x and y greater than 0 and less than 4")
            continue
        if field[y-1][x-1] != ' ':
            print("Cell is occupied")
            continue
        else:
            return x, y

def check_win():
   for i in range(3):
      if field[i] == ['X', 'X', 'X']:
         print('X is win!!!')
         return True
      if field[i] == ['0', '0', '0']:
         print('0 is win!!!')
         return True
   for i in range(3):
       simb = []
       for j in range(3):
           simb.append(field[j][i])
       if simb == ['X', 'X', 'X']:
           print('X is win!!!')
           return True
       if simb == ['0', '0', '0']:
           print('0 is win!!!')
           return True
   simb = []
   for i in range(3):
       simb.append(field[i][i])
   if simb == ['X', 'X', 'X']:
       print('X is win!!!')
       return True
   if simb == ['0', '0', '0']:
       print('0 is win!!!')
       return True
   simb = []
   for i in range(3):
       simb.append(field[i][2-i])
   if simb == ['X', 'X', 'X']:
       print('X is win!!!')
       return True
   if simb == ['0', '0', '0']:
       print('0 is win!!!')
       return True

startgreet()

field = [[' ']*3 for i in range(3)]

num_move = 0
while True:
    show_field()
    num_move += 1
    if num_move % 2 != 0:
        print("X - move")
    else:
        print("O - move")
    x, y = enter_cords()
    if num_move % 2 != 0:
        field[y-1][x-1] = 'X'
    else:
        field[y-1][x-1] = '0'
    if check_win():
        show_field()
        break
    if num_move == 9:
        print('Draw!!!')
        break
    


