from cat import Cat


class Dog:
    # pass

    kind = "corgi"  # class variable

    # special method called during initialization
    # similar to constructor
    # self gives access to attributes and methods in class
    # self is similar to "this" from Java
    # convention: first argument, call whatever you like
    def __init__(self, name):
        self.name = name

    def ageset(self, age):
        self.age = age


d0 = Dog("Bingo")
# d0.name = "Bingo"
d0.ageset(1)
print(d0.name, d0.kind, d0.age)

d1 = Dog("Brutus")
d1.ageset(4)
print(d1.name, d1.kind, d1.age)

c1 = Cat("Shrimp")
print(c1.name)
