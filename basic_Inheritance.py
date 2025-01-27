# Parent class
class Animal:
    def speak(self):
        return "I make a sound"

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

# Creating an object of Dog class
dog = Dog()
print(dog.speak())  # Output: Woof! Woof!
