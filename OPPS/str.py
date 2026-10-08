class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"   # CTRL + / 
s1=Person("diwakar",20)
print(s1)