# done via three ways - 1 code duplication
# 2 - explicit call
# 3 - calling super() method

class baseChai():
    def __init__(self,q,type_):
        self.quantity = q
        self.type = type_
class MasalaChai(baseChai):
    def __init__(self,q,type_,sugar_lvl):
        self.quantity = q
        self.type = type_
        self.sugar = sugar_lvl
class MasalaChai(baseChai):
    def __init__(self,q,type_,sugar_lvl):
        baseChai.__init__(q,type_)
        self.sugar = sugar_lvl        