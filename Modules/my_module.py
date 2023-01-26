test_var = 'test'

def test_function(content):
    print(f"This is an imported function with the parameter: {content}")

class Test:
    def __int__(self):
        self.name = 'My App'
        self.value = 12

    def do_something(self):
        print('Hello')


def sum_calculator(*args):
    # without *   --> args instead *args
    return sum(args)