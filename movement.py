i = 2
j = 2
a = [['x' if k == i and l == j else '-' for k in range(5)] for l in range(5)]

for m in a:
    print(*m)


def pitch(move_s=0, move_v=0):
    global i, j, a
    if move_s and (i != 0 or i != 4):
        i += move_s
        a = [['x' if k == i and l == j else '-' for k in range(5)] for l in range(5)]
        return i, a
    elif move_v:
        j += move_v
        a = [['x' if k == i and l == j else '-' for k in range(5)] for l in range(5)]
        return j, a


def movement(move):
    if move == 'a' and i == 0:
        pitch(0, 0)
    elif move == 'a':
        pitch(-1, 0)
    elif move == 'd' and i == 4:
        pitch(0, 0)
    elif move == 'd':
        pitch(1, 0)
    elif move == 'w' and j == 0:
        pitch(0, 0)
    elif move == 'w':
        pitch(0, -1)
    elif move == 's' and j == 4:
        pitch(0, 0)
    else:
        pitch(0, 1)


while True:
    c = input()
    movement(c)
    for m in a:
        print(*m)