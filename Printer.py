class Printer(object):
    def __init__(self):
        self.values=[]

    def log(self, *values):
        for i in values:
            self.values.append(i)
            print(i, end=' ')


class FormattedPrinter(Printer):

    def new_log(self, *values):
        print('*****')
        self.log(*values)
        print('*****')



p1=Printer()
#p1.log(1, 2, 3)

p2=FormattedPrinter()
p2.new_log(1, 2, 3)