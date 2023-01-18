# -----------------------------
#           Lesson 1
# -----------------------------

# A function is simply a block of code that can be reused
# 1. We create the function, this is where all the code is added
# 2. We call the function, this executes the code created in step 1
# A function can be called multiple times and we can even customise it when we call it

def test_function():
    print("Hello")
    test = 1 + 2
    print(test)

def calculator(num1, num2):
    result = num1 + num2
    print(result)

test_function()
calculator(2, 5)
calculator(10, 5)
# print(num1) Error
# print(num1) Error
print('\n'*3)

# -----------------------------
#           Exercise
# -----------------------------

def better_calculator(num1, num2, operator):
    match operator:
        case 'plus':
            result = num1 + num2
        case 'minus':
            result = num1 - num2
        case _:
            result = "Wrong operator"

    print(result)

better_calculator(1, 2, 'plus')
better_calculator(50, 5, 'minus')
better_calculator(50, 10, 'divide')
print('\n'*5)




# -----------------------------
#           Lesson 2
# -----------------------------

# When a function is created we can set parameters     --->    def test_function(parameter1, parameter2):
# These parameters can be used like variables inside of the function (these parameters only exists inside of the function)

# When calling the function you can add an argument to give the parameter a value      --->     test_function('hello', 42)




# Arguments are assigned to parameters by position (default)
# You can also use keyword arguments to be more precise



def test_function2(arg1 = "Argument 1", arg2 = "Argument 2", arg3 = "Argument 3", arg4 = "Argument 4"):
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)
    print("")

test_function2(arg1 = 1, arg2= "Hello", arg3 = True, arg4 = [1, "2", "test"])

test_function2(arg4 = 1, arg2= "Hello", arg1 = True, arg3 = [1, "2", "test"])

test_function2(arg4 = 1,
               arg2= "Hello",
               arg1 = True,
               arg3 = [1, "2", "test"])

# Positional arguments always have to come before keyword
test_function2(1, arg2= "Hello", arg3 = True, arg4 = [1, "2", "test"])


# Default argument
test_function2(10, arg2="Hi", arg3=False)
test_function2()

# -----------------------------
#           Exercise
# -----------------------------

# Create greeter function with 3 arguments: person, greet and weekday
# person and greet should have default arguments ('Person' for person and 'Hello' for greet)
# inside of the function use an f-string to print the greet and the person and also print the weekday
# when calling the function, use at least one positional argument and 1 keyword argument

def greeter(weekday, person = "Person", greet="Hello"):
    print(f"{greet} {person} Weekday: {weekday}")

greeter("Tuesday", "Bob", greet="Hi")
greeter("Monday", greet="Hola")
print('\n'*3)





# -----------------------------
#           Lesson 3
# -----------------------------

# What if you don't know the number of arguments?
# def print_all(arguments):
#     # print all arguments
#     for argument in arguments:
#         print(argument)
#
# print_all([1,2,3,4,5,'hello'])

# list unpacking
# we are adding a star before the parameter that we want to unpack
def print_all(first, *arguments, extra):
    print(first)
    print(arguments)
    print(extra)
    for argument in arguments:
        print(argument)

print_all(1,2,3,4,5,'hello',123,534,extra=21)
print('\n')

# keyword unpacking
# double star - looks for keyword arguments and then unpacks all of them inside of a dictionary
def print_more(**arguments):
    print(arguments)

print_more(arg1 = '1', arg2= '2', arg3 = [1,2,3], arg4='test')
print('\n')


def print_even_more(*args, **kwargs):
    print(args)
    print(kwargs)

print_even_more(1,2,3,4,5,'Hello',True, test=1, test2="Hi")

# -----------------------------
#           Exercise
# -----------------------------
# create a calculator function that prints the sum of an unlimited amount of numbers

def calculator2(*args):
    # result = int()
    # for x in args:
    #     result += x
    # print(result)

    result = sum(args)
    print(result)

calculator2(1,2,3,4,5)
print('\n'*4)

# -----------------------------
#           Lesson 4
# -----------------------------

# Functions and scope
# Variables created inside of a function are only available inside of that function
# This is called a 'local scope'

# Creating variables outside of functions is the 'global scope'

a = 10
def test_func():
    a=2
    print(a)
test_func()

def test_func_2():
    a = 200
    print(a)

test_func_2()

# def test_func_3():
#     global a
#     a += 2
#     print(a)

def test_func_3(a):
    a += 2
    # print(a)
    return a

# print(test_func_3(a))
a = test_func_3(a)
print(a)

# Functions are supposed to separate from the rest of the code
# Once the code becomes more complex it is really easy to run out of variable names
# For example, with the car, both the battery and the tank might have a 'capacity' variable

# Local scopes inside of a function help to keep things organised


# Rules of scope:
# Every function has its own local scope & every local scope is separate
# Global variables can be accessed in the local scope but they cannot be changed(or created)
# You can move between scopes with parameters, global and return but only use it when needed



# -----------------------------
#           Exercise
# -----------------------------
multiplier = 2
has_calculated = False

def multiply_calculator(number):
    global has_calculated
    result = number*multiplier
    has_calculated = True
    return result

print(multiply_calculator(3))
print(has_calculated)
print("\n"*3)


# -----------------------------
#           Lesson 5
# -----------------------------
# Lambdas - single line functions

# lambda para: expression
# for example
# lambda x: x+1
# The result is automatically returned


a = lambda x: x + 1
simple_calc = lambda a, b: a + b
print(a(10))
print(simple_calc(2,3))

# Why we use it:
# - some functions want other functions as argument
#   sort([1, 4, 3, 8, 2], func)   -- func would usually be a lambda

# - graphical user interfaces


# -----------------------------
#           Exercise
# -----------------------------
# create a lambda function that accepts 1 intiger argument
# if the integer is > 5 return hello
# otherwise return bye
b = lambda x: "hello" if x > 5 else "bye"
print(b(7))
print(b(2))
print('\n'*3)




# -----------------------------
#           Lesson 6
# -----------------------------


# Documenting functions


# Functions can get complicated so you want to explain it
# You can either add an explainer text this is called a docstring
# You can also hint at what types of data you expect for the parameters and the return value


def test(a: int = 10,b: int = 0) -> int:
    # docstring
    '''A simple function that prints 2 parameters'''
    print(a)
    print(b)
    return a + b

test(1,2)
print(test.__doc__)
help(test)