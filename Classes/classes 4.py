# -----------------------------
#           Lesson 5
# -----------------------------
# Classes and scope


# Since every method has a reference to the class it is easy to get and change class attributes
# Because of that, methods rely much less on parameters, global and return (although you can use it)
# Objects can even be influence from the outside and from a local scope of a function!

# scope problem

def update_health(amount):
    monster.health += amount
#
# health = 10
# print(health)
# update_health(20)
# print(health)

class Monster:
    def __init__(self, health, energy):
        self.health = health

        # 1:
        # self.energy = self.set_energy(energy)
        # 2:
        self.set_energy(energy)
    def update_energy(self, amount):
        self.energy += amount

    def set_energy(self, energy):
        new_energy = energy * 2 + 1

        # 1:
        # return new_energy
        # 2:
        self.energy = new_energy

monster = Monster(health = 100,energy = 50)
# print(monster.health)
# monster.health += 20
# print(monster.health)

# update_health(20)
# print(monster.health)

# monster.update_energy(30)
print(monster.energy)

print("\n")
# -----------------------------
#           Exercise
# -----------------------------
# 1. Create a Hero class with 2 parameters: damage, monster(pass the monster object)
# 2. The Monster class should have a method that lowers the health -> get_damage(amount)
# 3. The Hero class should have an attack method that calls the get_damage method from the monster the amount of damage is hero.damage

class Monster2:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def update_energy(self, amount):
        self.energy += amount

    def get_damage(self, amount):
        self.health -= amount

class Hero:
    def __init__(self, damage, monster):
        self.damage = damage
        self.monster = monster

    def attack(self):
        self.monster.get_damage(self.damage)

monster2 = Monster2(health = 200, energy = 40)
hero = Hero(damage = 20,monster = monster2)
print(monster2.health)
hero.attack()
print(monster2.health)