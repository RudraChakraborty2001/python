# Parent class
class Animal:
    def speak(self):
        return "I make a sound"

# Child classes override the method
class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow! Meow!"

# Using polymorphism
def make_sound(animal):
    print(animal.speak())

make_sound(Dog())  # Output: Woof! Woof!
make_sound(Cat())  # Output: Meow! Meow!
