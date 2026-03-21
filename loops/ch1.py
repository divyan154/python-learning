# usage of zip
names = ["Joi","Manta","Yamada","Tanaka"]

prices = ['10','30','304','40']

date = ['Today',"Yesterday","Tomorrow","today"]
for name,price,day in zip(names,prices,date):
    print(f"{name} paid {price} on {day}")