# -----------------------------
#           Lesson 3
# -----------------------------
# Custom modules / creating modules


# The main reason to create your own modules is organization
# Each module is in a separate file and that way you never have too much stuff at once


import my_module

print(my_module.test_var)
my_module.test_function(123)
test_object = my_module.Test()
test_object.do_something()


print('\n'*2)
# -----------------------------
#           Exercise
# -----------------------------
# Create a sum calculator function that takes unlimited arguments and returns the sum
# create it in my_module.py file and run here

print(my_module.sum_calculator(1, 2, 3, 4, 5))