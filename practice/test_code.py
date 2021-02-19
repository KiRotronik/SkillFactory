class Player:


    def move(self):
        a, b = User.ask()
        return a, b



class User(Player):
    @staticmethod
    def ask():
        while True:
            cords = input("Enter x,y coordinates for shoot").split()
            if len(cords) != 2:
                print("Enter two digits from 1 to 6")
                continue
            x, y = cords
            if not x.isdigit() and y.isdigit():
                print("Enter two digits from 1 to 6")
                continue
            x, y = int(x), int(y)
            if x < 1 or x > 6 and y < 1 or y > 6:
                print("Enter two digits from 1 to 6")
                continue
            else:
                return x, y

print(Player.move())


