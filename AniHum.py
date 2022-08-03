class Animal(object):
    def __init__(self, name, agression):
        self.name = name
        self.agression = agression

    def attack_human(self, other):
        if not other.agression and self.agression:
            other.danger.append(self.name)
            print(self.name, 'Opasen dlya', other.name)
        else:
            print(self.name, 'Ne opasen dlya', other.name)



class Human(Animal):
    def __init__(self, name, agression):
        self.name = name
        self.agression = agression
        self.danger = []

    def is_dangerous(self, other):
        if other.name in self.danger:
            return 'Yes'
        else:
            return "No"


hercules = Human('Геракл', True)
prometeus = Human('Прометей', False)

hydra = Animal('Гидра', True)
hawk = Animal('Ястреб', True)
lamb = Animal('Овца', False)
print('\nПолучение людьми опыта общения с животными:\n ')
hydra.attack_human(hercules)
hawk.attack_human(hercules)
lamb.attack_human(hercules)

hydra.attack_human(prometeus)
hawk.attack_human(prometeus)
lamb.attack_human(prometeus)

print('\nПолучение людьми опыта общения с другими людьми:\n ')
hercules.attack_human(prometeus)

print('\nПроверка накопленного людьми опыта общения с животными:\n ')
print('Опасна ли {} для {}? : {}'.format(hydra.name, hercules.name, hercules.is_dangerous(hydra)))
print('Опасен ли {} для {}? : {}'.format(hawk.name, hercules.name, hercules.is_dangerous(hawk)))
print('Опасна ли {} для {}? : {}'.format(lamb.name, hercules.name, hercules.is_dangerous(lamb)))

print('Опасна ли {} для {}? : {}'.format(hydra.name, prometeus.name, prometeus.is_dangerous(hydra)))
print('Опасен ли {} для {}? : {}'.format(hawk.name, prometeus.name, prometeus.is_dangerous(hawk)))
print('Опасна ли {} для {}? : {}'.format(lamb.name, prometeus.name, prometeus.is_dangerous(lamb)))

print('\nПроверка накопленного людьми опыта общения с другими людьми:\n ')
print('Опасен ли {} для {}? : {}'.format(hercules.name, prometeus.name, prometeus.is_dangerous(hercules)))
