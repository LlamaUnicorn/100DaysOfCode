# def add(*args):
#     print(type(args) # tuple
#     print(args[0])
#     n = 0
#     for i in args:
#         n += i
#     return n
#
#
# print(add(1, 2, 3))


def calculate(n, **kwargs):
    # print(type(kwargs)) # type dictionary
    # print(kwargs['add']) # value
    # The same as above ^
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw['make']
        self.model = kw.get['model']

my_car = Car(make='Nissan', model='GT-R')
print(my_car.model)

# If we don't provide 2 kwargs when calling a function it crashes
# my_car = Car(make='Nissan') # KeyError: 'model'
# Use "get" instead: kw.get['model']
# If the argument doesn't exist "get" will prevent the crash
print(my_car.model)
