# -----------------------------
#           Lesson 4
# -----------------------------
# Classes and methods


# Everything in python is an object
# Including the inbuilt strings, integers etc
# Even functions are objects

# A function and a method both execute a block of code
# The difference is that a method belongs to an object


# test = 'a'
# def test():
#     pass
#
# a = test
# a.another_attribute = 10
#
# print(dir(test))
# print(dir(a))

def add(a, b):
    return a + b

class Test:
    def __init__(self, add_function):
        self.add_function = add_function

test = Test(add_function = add)
print(test.add_function(1, 2))

print("\n")
# -----------------------------
#           Exercise
# -----------------------------
# 1. Create a Monster class with a parameter called func, store this func as parameter

class Monster:
    def __init__(self, func):
        self.my_function = func

# 2. Create another class, called Attacks, that has 4 methods: bite, strike, slash, kick (each method just prints some text)

class Attacks:
    def bite(self):
        print("Bite!")
    def strike(self):
        print("Strike!")
    def slash(self):
        print("Slash!")
    def kick(self):
        print("Kick!")

test_attacks = Attacks()
test_attacks.bite()
test_attacks.kick()
test_attacks.slash()
test_attacks.strike()
print('\n')

# 3. Create a monster object and give it one of the attack methods from the attacks class

monster = Monster(func = Attacks().bite)
monster.my_function()
# or
# attacks =Attacks()
# monster = Monster(func= attacks.bite())
# monster.my_function()
