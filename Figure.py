class Figure:
    def __init__(self, lst):
        self.lst = lst

    def checking(self):
        figures = {1: self.sq, 2: self.rect, 3: self.triang}
        figures[len(self.lst)]()

    def sq(self):
        print('Sq square: ', (self.lst[0]) ** 2)
        print('Sq perim: ', self.lst[0] * 4)

    def rect(self):
        print('Rect square: ', self.lst[0] * self.lst[1])
        print('Rect perim: ', (sum(self.lst)) * 2)

    def triang(self):
        if self.lst[0] + self.lst[1] <= self.lst[2] or self.lst[0] + self.lst[2] <= self.lst[1] or self.lst[2] + \
                self.lst[1] <= self.lst[0]:
            self.lst = list(map(int, input('insert valid number: ').split()))
            self.checking()
        else:
            p = sum(self.lst) / 2
            squ = (p * (p - self.lst[0]) * (p - self.lst[1]) * (p - self.lst[2])) ** (1 / 2)
            print('Tr square: {:.2f}'.format(squ))
            print('Tr perim: ', p * 2)


a = Figure(list(map(int, input('insert number: ').split())))

a.checking()
