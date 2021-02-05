class Event:
    def __init__(self, name):
        self.n = name


class Sup(Event):
    def __init__(self, name, family):
        super().__init__(name)
        self.f = family


test = Sup('Serge', 'Super')

print(test.n)
