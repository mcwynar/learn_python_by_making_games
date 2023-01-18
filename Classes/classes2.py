# -----------------------------
#           Lesson 3
# -----------------------------
# Dunder

# __Dunder__ methods
# (double underscore methods)

# A dunder method is a method that is not called by the user
# Instead, it is called by python when something happens for example:
# __init__ is called when the object is created
# __len__ is called when the object is passed into len()
# __abs__ is called when the object is passed into abs()


class Monster:

    def __init__(self, health, energy):
        print('The monster was created')
        self.health = health
        self.energy = energy

    def __len__(self):
        return self.health

    def __abs__(self):
        return self.energy

    def __call__(self):
        print('The monster was called')

    def __add__(self, other):
        return self.health + other

    def __str__(self):
        return f"A monster with health {self.health} and energy {self.energy}"

    # methods
    def attack(self, amount):
        print('The monster has attacked')
        print(f'{amount} of damage was dealt')
        self.energy -= 20
        print(f'Monster energy {self.energy}')

    def move(self, speed):
        print(f'The monster has moved! It has a speed of {speed}')

monster1 = Monster(10, 20)
# monster2 = Monster(health = 50, energy = 100)

# print(monster1.health)
# print(monster2.health)

print(len(monster1))
print(abs(monster1))
print(dir(monster1))

print(monster1.__dict__)
print(vars(monster1))

# __call__
monster1()
# __add__
print(monster1 + 100)
# __str__
print(monster1)