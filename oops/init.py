# How to use constructor 

class ChaiOrder:
    def __init__(self,type_,quantity):
        self.type = type_
        self.quantity = quantity

    def summary(self):
        return f"{self.quantity}ml for {self.type} Chai"    

order = ChaiOrder("Masala",100)
order2 = ChaiOrder("Green",200)
print(order.summary())
print(order2.summary())


