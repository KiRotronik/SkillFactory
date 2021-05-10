class NonPositiveDigitException(ValueError):
    print("The side of the square must be greater than 0")


class Square:
    def __init__(self, side):
        if side <= 0:
            raise NonPositiveDigitException()
        else:
            self.side = side

