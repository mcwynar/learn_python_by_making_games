# -----------------------------
#           Exercise
# -----------------------------
# Create a decorator that executes the function twice
# 3 decorators in total
import time
def decorator(func):
    def wrapper():
        print('Decoration begins')
        func()
        print('Decoration ends')
    return wrapper

def duration_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        duration = time.time() - start_time
        print(f'Duration {duration}')
    return wrapper

def call_twice_decorator(func):
    def wrapper():
        func()
        func()
    return wrapper

@call_twice_decorator
@decorator
@duration_decorator
def func():
    print('Function')
    time.sleep(1)
func()