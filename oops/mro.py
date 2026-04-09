# Method resolution order in case of multiple inheritance

class A:
    label = "A..."

class B(A):
    label = "Masala Chai..."

class C(A):
    label = "Herbal Tea"

class D(C,B):
    pass
    # label = "D..."

# what will label method of D class print ? Masala Chai.. or Herbal tea
cup = D()
print(cup.label)#prints first inherited class method in this case C
