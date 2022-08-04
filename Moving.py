class Desk(object):
    def __init__(self, i):
        self.i = i
        self.j = i
        self.matr = []

    def pitch(self, move_s=0, move_v=0):
        if move_s:
            self.i += move_s
            self.matr = [['x' if k == self.i and l == self.j else '-' for k in range(5)] for l in range(5)]

        elif move_v:
            self.j += move_v
            self.matr = [['x' if k == self.i and l == self.j else '-' for k in range(5)] for l in range(5)]

    def movement(self, move):
        if move == 'a' and self.i == 0:
            self.pitch(0)
        elif move == 'a':
            self.pitch(-1)
        elif move == 'd' and self.i == 4:
            self.pitch(0)
        elif move == 'd':
            self.pitch(1)
        elif move == 'w' and self.j == 0:
            self.pitch(move_v=0)
        elif move == 'w':
            self.pitch(move_v=-1)
        elif move == 's' and self.j == 4:
            self.pitch(move_v=0)
        else:
            self.pitch(move_v=1)


desk = Desk(3)

while True:
    c = input()
    desk.movement(c)
    for m in desk.matr:
        print(*m)
