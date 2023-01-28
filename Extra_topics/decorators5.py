# Decorators inside of classes

# @property
# @property allows you to turn methods into attributes
# This comes from the property function

from datetime import datetime
# class Generic:
#     def __init__(self):
#         self._x = 10
#
#     def getter(self):
#         print('Get X')
#         print(datetime.now())
#         return self._x
#     def setter(self, value):
#         print('Set X')
#         self._x = value
#     def deleter(self):
#         print('Delete X')
#         del self._x
#
#     #           getting, setting, deleting
#     x = property(getter, setter, deleter)

# generic = Generic()
# generic.x = 4
# print(generic.x)
# del generic.x



# using decorator

class Generic:
    def __init__(self):
        self._x = 10

    @property
    def x(self):
        print('Get X')
        print(datetime.now())
        return self._x
    @x.setter
    def x(self, value):
        print('Set X')
        self._x = value
    @x.deleter
    def x(self):
        print('Delete X')
        del self._x

generic = Generic()
generic.x = 4
print(generic.x)
del generic.x

