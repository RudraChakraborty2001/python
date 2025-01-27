# Grandparent class
class Grandparent:
    def greet(self):
        return "Hello from Grandparent"

# Parent class inheriting from Grandparent
class Parent(Grandparent):
    def show(self):
        return "I am the Parent"

# Child class inheriting from Parent
class Child(Parent):
    def display(self):
        return "I am the Child"

# Creating an object of Child class
c = Child()
print(c.greet())   # Output: Hello from Grandparent
print(c.show())    # Output: I am the Parent
print(c.display()) # Output: I am the Child
