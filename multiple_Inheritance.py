# Parent class 1
class Father:
    def work(self):
        return "Father is working"

# Parent class 2
class Mother:
    def cook(self):
        return "Mother is cooking"

# Child class inheriting from both parents
class Child(Father, Mother):
    def play(self):
        return "Child is playing"

# Creating object
c = Child()
print(c.work())  # Output: Father is working
print(c.cook())  # Output: Mother is cooking
print(c.play())  # Output: Child is playing
