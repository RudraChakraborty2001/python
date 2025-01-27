#inheritence = Allows a class to inherit attributes abd methods from another class 
# Helps with code reusability and extensibility 
# class Child(Parent) 

class Animal:

    def __init__(self, name):
        self.name = name
        self.is_alive =True   
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    pass            

class Cat(Animal):
    pass

class Mouse(Animal):
    pass

dog = Dog("leeo")
cat = Cat("mini")
mouse = Mouse("miki")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
