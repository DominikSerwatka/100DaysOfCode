# Function that take many arguments
def add(*args):
    print(args[0])
    print(type(args))
    print(args)
    final = 0
    for n in args:
        final += n
    return final


print(add(1, 4, 5))


def calculate(n, **kwargs):
    print(type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)
    print(kwargs["add"], kwargs["multiply"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        self.make = kw["make"]
        self.model = kw.get("model")

#
# my_car = Car(make="Nissan", model="GT-R")
# print(my_car.model)

my_car = Car(make="Nissan")
print(my_car.model)


def function_test(function):
    function()


def test():
    print("function test")


function_test(test)