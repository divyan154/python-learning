# Decorators are wrappers around a function that modifies the behaviour or keeps same anything

from functools import wraps #way to preserve metadata
def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper    

@my_decorator
def greet():
    print( "Hello My name is Divyansh Sharma")

greet()
print(greet.__name__)