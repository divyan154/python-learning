nums = [1 , 3 , 6 , 9 , 2 , 6]
def filterFunction(num):
    """Prints odd numbers """
    if(num % 2):
        print(num)

for n in nums:
    # print(filterFunction(n).__doc__)
    # filterFunction(n).__str__
    filterFunction(n)


# filterFunction
print(filterFunction.__doc__)