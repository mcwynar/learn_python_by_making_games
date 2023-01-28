# -----------------------------
#           Lesson 4
# -----------------------------
# Eval + Exec

# Eval and exec are special functions that translate strings into python code
# Eval('1+1') --> returns 1+1 (i.e. 2)
# You can even use it to create new variables
# This can give you a ton of flexibility

# !!! be careful when using exec or eval
# If nahded badly they allow users to run their own code
# If you run a database, they might steal all of it
# For example, you might have an input field designed for entering names and you process those names with eval or exec
# Instead of writing a name, a user could enter code to access your data


# Eval
# Is less powerful: It can only evaluate code. Which means it can run functions and simple operations but it cannot create new variables

# Exec
# Is more powerful: It can execute any code. You can create variables, run functions etc

print(eval('5+10'))
print(eval('"test".upper()'))

exec('if True: print("Test")')
exec('a = 10')
print(a)

print('\n')
my_string = 'test'
print(my_string.upper())
print(my_string.title())
print(my_string.lower())
print(my_string.casefold())

print()
# -----------------------------
#           Exercise
# -----------------------------
# Express this four lines above using eval statement and for loop

list_of_actions = ['upper', 'title', 'lower', 'casefold']
for value in list_of_actions:
    print(eval(f'my_string.{value}()'))