# -----------------------------
#           Lesson 3
# -----------------------------
# Decorators

# Decorators are functions that 'decorate' other functions
# We essentially wrap a function around another function
#
#
# normal function         call function
# def func():        -->    func()
#    ...
#
#
# decorator func        we are calling the decorator function and inside of that decorator function we are calling the original function
# def func():       -->  func(func())
#    ...

# That way we can give a function extra functionality without changing it
# For example, we can create a decorator for a function that makes the function execute twice when called

# You usually use them in 3 circumstances:
# - you want to test your code without changing it
# - you are working in a team and want to avoid unnecessary code changes
# - decorators in classes allow you to run code when an attribute is accessed or changed

# They are good practice to understand how to pass functions around via the return statement

def func():
    print('Function')

def wrapper(func):
    print('Hello')
    func()
    print('Goodbye')

# print(func)
wrapper(func)


def function_generator():
    def new_function():
        print('New function')
    return new_function

new_func = function_generator()
new_func()
