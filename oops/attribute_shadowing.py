class Student:
    school = "Spring Dales School"
    # subjects=["Maths","English"]
    medium = "English"


anish = Student()

anish.medium= "Hindi"
anish.house = "green"
print(anish.house)
del anish.medium
del anish.house
print(f"After delete {anish.medium}")
print(f"After deleting house {anish.house}")