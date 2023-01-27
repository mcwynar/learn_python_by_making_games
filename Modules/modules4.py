# -----------------------------
#           Lesson 4
# -----------------------------
# Dunder main
# __main__

# When a python file is called it creates a few internal variables
# The most used one is __name__

# The currently executed file __name__ == '__main__'
# Any imported file __name__ == '__filename__'
# This helps us control what code is executed

import my_module
# print(__name__)

if __name__ == '__main__':
    print('the main file')