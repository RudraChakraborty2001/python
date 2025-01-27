class Dog:
    def sound(self):
        return "Woof! Woof!"

class Cat:
    def sound(self):
        return "Meow! Meow!"

# Using polymorphism
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.sound())

# Output:
# Woof! Woof!
# Meow! Meow!
