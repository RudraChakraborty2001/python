from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Child classes must implement the abstract method
class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow! Meow!"

# Objects
dog = Dog()
cat = Cat()

print(dog.speak())  # Output: Woof! Woof!
print(cat.speak())  # Output: Meow! Meow!
