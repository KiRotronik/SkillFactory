class Event:
    def __init__(self, name, pame):
        self.n = name
        self.p = pame


class Sup(Event):
    def __init__(self, name, pame, family):
        super().__init__(name, pame)
        self.f = family


test = Sup('Serge', 'Super', 'Super')

print(test.n)
