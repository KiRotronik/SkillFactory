class Moon:

    def __eq__(self, other):
        return self.value == other


class Earth:

    def __eq__(self, other):
        return self.value == other


a = Earth()
b = Moon()

a.value = 3
b.value = 3
print(a == b)