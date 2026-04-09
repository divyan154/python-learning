# Class methods and Static methods:
# Class method can be used to somehow modify the constructor
# Special points - Alwyas take first argument cls
class ChaiOrders:
    def __init__(self,Chai_type,sweetness,size):
        self.Chai_type = Chai_type
        self.sweetness = sweetness
        self.size = size
    @classmethod
    def Dict(cls,order_data):
        return cls(order_data["Chai_type"],order_data["sweetness"],order_data["size"])
    @classmethod
    def String(cls,order_string):
        Chai_type,sweetness,size = order_string.split(",")
        return cls(Chai_type,sweetness,size)    

class sizeCheck:
    pass
    @staticmethod
    def sizechk(size):
        return size in ["small","medium","large"]


print(sizeCheck.sizechk("medium"))
order1 = ChaiOrders.Dict( {"Chai_type":"Masala","sweetness":"Medium","size":"Small"})
order2 = ChaiOrders.String("Ginger  , high , large")
# print(order1.__dict__)
print(order2.__dict__)
