# -----------------------------
#           Lesson 1
# -----------------------------
# Intro

# Modules are extra parts that we can attach to our programs
# For example, if we wanted random numbers we would add the random module
# We can also create our own modules (across multiple files) to make the code more organised


# Adding extra parts
# 1. You can import from the python standard library. These are preinstalled with python
# 2. You can import additional modules made by other people but those you need to install on your computer first


# Python standard library


import string

from random import *

#import multiple modules
# import string, random, math

from math import sin

from math import floor as get_floor



print(string.ascii_lowercase)

random_number = randint(0, 10)
print(random_number)

test_list = [1, 'hello', 2, False, 3, [0, 10, 100], 4, {"one": 1, "two": 2}, 5, 0.51235010, 6]
print(choice(test_list))

print(sin(1))
print(get_floor(4.9))


print('\n'*2)
# -----------------------------
#           Exercise
# -----------------------------
# Get current time from datetime
# from datetime import now
from datetime import datetime as dt
print(dt.now())
