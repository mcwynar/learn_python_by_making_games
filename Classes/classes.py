# -----------------------------
#           Lesson 1
# -----------------------------
# Intro


# An object is a container for variables and functions
#
# For example, a monster object might contain:
# Variables for health, energy, stamina, damage
# Functions for attack, movement, animations


# Although, they have special names
# Variables in an object are called attributes
# Functions in an object are called methods

# It is possible to have multiple objects
# For example, we could create three different monsters and each of this monsters could have customized attributes
# however, this does not apply to methods:

#  Monster1              Monster2                Monster3
#  health = 90           health = 60             health = 40          <--   custom
#  energy = 20           energy = 40             energy = 10          <-- attributes
#
#  attack                attack                  attack               <--  same     not exactly this same                                    (can be customized to an extent,
#  move                  move                    move                 <-- methods   because they always apply to their respective object      but not nearly as much as the attributes)

# Each object has its own attributes and methods

# Objects can also interact with each other



# Object-oriented programming (OOP)
#
# Your code is organised via object
# Almost all large projects (in any coding language) are organised like that

# What are classes?
# A class is the blueprint for an object
# When creating an object we first need a class
# A class also accepts arguments to customise the object

# Class                         Object
# Monster                       Monster
# health = ?                    health = 90
# energy = ?                    energy = 20
#               --------->
# attack                        attack
# move                          move

# A class can also inherit from another class
# The resulting objects will have attributes and methods from both classes
#
# For example we want to create a shark class
# Monster                       Shark                           Shark
# health = ?                    speed = ?                       health = 90
# energy = ?        Inherit                     create object   energy =20
#                   ------->                    ------------->  speed = 100
# attack                        bite
# move                                                          attack
#                                                               move
#                                                               bite


# Why use classes & objects?
# 1. They organise complex code
# 2. They help to create reusable code
# 3. They are used everywhere
# 4. Some modules require you to create classes
# 5.They make it easier to work with scope



# -----------------------------
#           Lesson 2
# -----------------------------
# Classes in practice

# CamelCase naming
class Monster:

    # attributes
    health = 90
    energy = 40

    # methods
    def attack(self, amount):
        # print(self)
        print('The monster has attacked')
        print(f'{amount} of damage was dealt')
        self.energy -= 20
        print(f'Monster energy {self.energy}')

    def move(self, speed):
        print(f'The monster has moved! It has a speed of {speed}')

monster = Monster()
print(monster.health)
print(monster.energy)
monster.attack(50)
monster.move(15)
