# Access a method without making instacne of class by using decorator
class Afk:
    @staticmethod
    def killed(text):
        return [item.strip() for item in text.split(",")]
    
# 1st way
# Hana = Afk()
# value = Hana.killed("Heaven  , 70 , 2")    

value = Afk.killed("Heaven  , 70 , 2")
print(value)