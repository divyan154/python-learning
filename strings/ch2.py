# #sets
# my_toys={"doremon",'zenitsu','tomnjerry'}
# toys={'naruto','zenitsu','kanjiro'}

# full_toys = my_toys | toys
# print(f"Full toys are {full_toys}")
# common_toys = my_toys & toys

# print(f"Common toys are {common_toys}")

# dict1 = {"name":"Divyansh","age":"20","sex":"male"}
# print(f"Dictionary is {dict1}")
# print(f"Dictionary itmes are  {dict1.items()}")
# print(f"Dictionary keys are  {dict1.keys()}")
# print(f"Dictionary values are  {dict1.values()}")

input_amount = int(input("Enter the amount order:"))
# print(f"Inupt amount type {type(input_amount)}")

delivery_fee = 0 if input_amount > 300 else 30

print(f"Delivery fee is : {delivery_fee}")
