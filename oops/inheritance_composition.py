
class BaseChai:
    def __init__(self,type_):
        self.type = type_

    def summary(self):
        print(f"Serving {self.type} Chai...")    

class MasalaChai(BaseChai):

    def __init__(self,quantity):
        self.quantity = quantity

    def serve():
        print("Adding Ginger , Cardamom, Sugar.....")  

class SpecialChai:
    base_chai = BaseChai
    def __init__(self):
        self.chai = self.base_chai("Ginger")
    def info(self):
        print(self.chai.summary())  

order = SpecialChai()
order.info()        

class randomChai(BaseChai):
    masala_chai = MasalaChai
    def __init__(self):
        self.chaii = self.masala_chai(300)
    def rando(self):
        print(self.chaii.serve())
order2 = randomChai()
print(order2.rando())

# regular instance methods called on objects = always need self parameter