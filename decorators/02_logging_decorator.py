from functools import wraps
def logger_decorator(func):
    wraps(func)
    def wrapper(*args,**kwargs):
        print(f"Before function executes")
        func(args)
        print(f"After function executes")
    return wrapper    


@logger_decorator
def my_func(name):
    print(f"Hello how are you. Watashi no namae wa {name}")

my_func("Divyansh")    
