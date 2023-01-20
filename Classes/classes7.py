# -----------------------------
#           Lesson 8
# -----------------------------
# Classes extra parts

class Monster:
    '''A monster that has some attributes'''
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

        # private attributes (it's just a convention; also work for methods)
        self._id = 5

    # methods
    def attack(self, amount):
        print('The monster has attacked!')
        print(f'{amount} damage was dealt')
        self.energy -= 20

    def move(self, speed):
        print('The monster has moved')
        print(f'It has a speed of {speed}')

monster = Monster(20, 10)
# print(monster._id)

# hasattr and setattr
# hasattr(object, 'attributeName')
print(hasattr(monster, 'health'))
print(hasattr(monster, 'weapon'))
if hasattr(monster, 'health'):
    print(f'The monster has {monster.health} health')
# setattr(object, 'attributeName', value)
# setattr(monster, 'weapon', 'Sword')
# print(monster.weapon)
new_attributes = (['weapon', 'Axe'], ['armor', 'Shield'], ['potion', 'Mana'])
for attr, value in new_attributes:
    setattr(monster, attr, value)
print(vars(monster))
print('\n\n')
# doc
print(monster.__doc__)
help(monster)
help(str)