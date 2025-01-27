# Parent class (Base class)
class Parent:
    def show(self):
        print("I am the Parent")

# Child class (Derived class) inheriting from Parent
class Child(Parent):
    pass  # Child class inherits everything from Parent

# Creating an object of Child class
c = Child()

# Calling the inherited method
c.show()  # Output: I am the Parent
