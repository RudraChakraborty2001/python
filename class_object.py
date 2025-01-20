#object = A "bundle" of related attributes (variables) and methods (functions) 
# Ex.. phone, cup, book 
# you need a "class" to create many object 
# class = (blueprint) used to design the structure and lay out of an object

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    

car1 = Car("Mustang", 2024, "red", False)

print(car1.model)
print(car1.year)
print(car1.for_sale)
