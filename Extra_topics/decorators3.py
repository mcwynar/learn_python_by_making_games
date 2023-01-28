# You can have functions with parameters being decorated
# Decorators themselves can also have parameters!

def decorator(func):
    def wrapper(*args, **kwargs):
        print('Decoration begins')
        func(*args, **kwargs)
        print('Decoration ends')
    return wrapper

@decorator  # or func = decorator(func)
def func(func_parameter):
    print(func_parameter)

func('Hello')