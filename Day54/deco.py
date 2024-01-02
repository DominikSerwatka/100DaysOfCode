# Python Decorator Function

def decorator_function(function):
    def wrapper_function():
        # add code before functions
        function()
        # add code after functions
    return wrapper_function

import time

def delay_decorator(function):
    def wrapper_function():
        print(type(function.__name__))
        print("from wrapper")
        time.sleep(5)
        function()
    return wrapper_function

@delay_decorator
def print_hello():
    print("hello world!")
    print("testtt")

def print_bye():
    print("Bye world")

print("test")
print_hello()
print("----------------")
output_func = delay_decorator(print_bye)
output_func()

