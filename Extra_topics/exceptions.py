# -----------------------------
#           Lesson 2
# -----------------------------
# Exceptions
# Error handling

# Your code should obviously not contain errors since those would crash the program
# However, sometimes you perform operations that might cause errors
# For that, Python has tools to anticipate errors and deal with them without crashing the program



# ----------------------------------------
#      Anticipating errors/exceptions
# ----------------------------------------
try:
    print(1/1)
    # print(a)
    # print(1/0)
except ZeroDivisionError:
    print('You cannot divide by 0')
except NameError:
    print('Does not exist')
else:
    # run only if the try statement doesn't have an error (we can think this is else  statement to except)
    print('The else statement')
finally:
    # run doesn't matter if we have exception or not
    print('finally...')

print('\n')
# ----------------------------------------
#            Raising exceptions
# ----------------------------------------
var_must_be_string = 'test'
if isinstance(var_must_be_string, str):
    print(var_must_be_string)
else:
    raise TypeError('Must be a string')

print('\n')
# Assert  - when condition is false whole program stops
a = 5
# assert a == 6


print('\n'*2)
# -----------------------------
#           Exercise
# -----------------------------
# Create a list and try to raise an Index error also add else and finally
exercise_list = [1, "Witaj", 2, True, 3]

try:
    print(exercise_list[5])
except Exception as err:
    print(f'We have a problem: {err}!')
else:
    print("It's a good value!")
finally:
    print('This is the end of our journey')