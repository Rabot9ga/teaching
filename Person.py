class Person(object):
    def __init__(self, age, name):
        self.age=age
        self.name=name
        self.persons=[]

    def know(self, person):
        if person.name not in self.persons:
            self.persons.append(person.name)
            person.persons.append(self.name)
        else:
            print("Persona uje v znakomix")

    def is_known(self, person):
        if person.name in self.persons:
            print('{} and {} know each other'.format(person.name, self.name))
        else:
            print('{} and {} are strangers'.format(person.name, self.name))


p1=Person(25, 'Nike')
p2=Person(23, "Bob")



p1.is_known(p2)

