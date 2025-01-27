#class variable = Shared among all instances of a class 
# Defined outside the constructor 
# Allow you to share data among all object created from the class

class Student:

    class__year = 2025

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Rudra", 25)
student2 = Student("Riya", 24)

print(student1.name)
print(student1.age)
print(student1.class__year)