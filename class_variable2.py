class Student:

    class__year = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students+=1
        
#see we have 2 student so num_students = 2
student1 = Student("Rudra", 25)
student2 = Student("Riya", 24)


# print(student1.name)
# print(student1.age)
# print(student1.class__year)
# print(Student.num_students)

print(f"My graduating class of {Student.class__year} has {Student.num_students} students")
print(student1.name)
print(student2.name)