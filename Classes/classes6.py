# -----------------------------
#           Lesson 7
# -----------------------------
# Complex inheritance

class Monster:
    def __init__(self, health, energy, **kwargs):
        print(f'Monster kwargs: {kwargs}')
        self.health = health
        self.energy = energy
        super().__init__(**kwargs)

    # methods
    def attack(self, amount):
        print('The monster has attacked!')
        print(f'{amount} damage was dealt')
        self.energy -= 20

    def move(self, speed):
        print('The monster has moved')
        print(f'It has a speed of {speed}')

class Fish:
    def __init__(self, speed, has_scales, **kwargs):
        print(f'Fish kwargs: {kwargs}')
        self.speed = speed
        self.has_scales = has_scales
        super().__init__(**kwargs)

    def swim(self):
        print(f'The fish is swimming at a speed of {self.speed}')

class Shark(Monster, Fish):
    def __init__(self, bite_strength, health, energy, speed, has_scales):
        self.bite_strength = bite_strength
        super().__init__(health = health, energy = energy,speed = speed, has_scales = has_scales)

# MRO (method resolution order)
# what order to parent in the methods of being called
print(Shark.mro())

# 1. Shark __init__
# 2. Monster __init__
# 3. Fish __init__
# We always need the super init method to go to the next item

shark = Shark(bite_strength = 50, health = 200, energy = 55, speed = 120, has_scales = False)
print(shark.speed)
print(shark.has_scales)
