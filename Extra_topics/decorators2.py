import time
def decorator(func):
    def wrapper():
        print('Decoration begins')
        func()
        print('Decoration ends')
    return wrapper

# shorthand
# @decorator
# def func():
#     print('Function')

# func = decorator(func)
# func()

def duration_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        duration = time.time() - start_time
        print(f'Duration {duration}')
    return wrapper

@decorator
@duration_decorator
def func():
    print('Function')
    time.sleep(1)
func()