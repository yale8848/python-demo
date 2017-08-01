from electric.ElectricCar import ElectricCar
from collections import OrderedDict

c = ElectricCar('elec')
c.addEnergy()

favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +language.title() + ".")

with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())
