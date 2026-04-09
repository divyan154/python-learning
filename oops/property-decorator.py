class JapaneseLevelOfMine:
    def __init__(self,level):
        self._level = level

    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self,level):
        if level in ["n3","n4","n5"]:
            self._level = level


Curr = JapaneseLevelOfMine("n5")
Curr.level = "n2"
print(Curr.level)