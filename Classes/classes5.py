# -----------------------------
#           Lesson 6
# -----------------------------
# Simple inheritance


# Inheritance means that 1 class gets attributes and methods from another class (or classes)

#  Monster                       Shark                           Shark
# health = ?                    speed = ?                       health = 90
# energy = ?                                                    energy = 20
#                   ------->                    ------------->  speed = 100
# attack                        bite
# move                                                          attack
#                                                               move
# PARENT                         CHILD                           OBJECT

# A class can inherit from an unlimited number of other classes
# A class can also be inherited from by an unlimited number of classes

# Inheritance, can get very complex
# However, most of the time you just need simple inheritance

class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    # methods
    def attack(self, amount):
        print('The monster has attacked!')
        print(f'{amount} damage was dealt')
        self.energy -= 20

    def move(self, speed):
        print('The monster has moved')
        print(f'It has a speed of {speed}')


#     newClass(what class we inherit from)
class Shark(Monster):
    def __init__(self, speed, health, energy):
        # Old way
        # Monster.__init__(self, health, energy)
        # or
        # New way
        super().__init__(health, energy)

        # super().move(10)
        self.speed = speed

    def bite(self):
        print('The shark has bitten')

    # overwrite parent method
    def move(self):
        print('The shark has moved')
        print(f'The speed of the shark is {self.speed}')

shark = Shark(speed= 120, health=100, energy=80)
print(shark)
print(f'Shark health: {shark.health}')
print(f'Shark energy: {shark.energy}')
print(f'Shark speed: {shark.speed}')
shark.bite()
print()
shark.attack(20)
print()
shark.move()


print("\n")
# -----------------------------
#           Exercise
# -----------------------------
# Create scorpion class that inherits from monster
# health and energy from the parent
# poison_damage attribute
# overwrite the damage method to show posion damage

class Scorpion(Monster):
    def __init__(self, poison_damage, health, energy):
        self.poison_damage = poison_damage
        super().__init__(health, energy)

    def damage(self):
        print("The scorpion has attacked!")
        print(f'{self.poison_damage} poison damage was dealt')

scorpion = Scorpion(poison_damage= 30, health= 170, energy= 90)
scorpion.damage()
print(scorpion.health)
