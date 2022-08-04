class Box(object):
    def __init__(self, volume):
        self.volume = volume

    def insert(self, other):
        if self.volume>=other.size:
            self.volume-=other.size
            print('Predmet polojen')
        else:
            print('Predmet polojit nelzya')


class Packet(Box):
    pass


class SomeObj(object):
    def __init__(self, size):
        self.size=size


