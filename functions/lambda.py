numbers = [ 1, 2 , 3 , 7 , 8 , 10]

even = list(filter(lambda num: num %2 == 0 ,numbers))
print(f"Event numbers are {even}")