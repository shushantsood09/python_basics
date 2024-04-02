class Student:
    # name = "Amit"
    # Default Constructor
    def __init__(self):
        print("Adding new student in Database..")
        pass
    college_Name = "ABC College" # Class Attribute
    name = "Shubham"  # Class Attribute

    # Parameterized constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding new student in Database..")

    def welcome(self):
        print("Welcome student", self.name)

    def getMarks(self):
        return self.marks

s1 = Student("Karan", 33)
print(s1.name) #Karan
print(s1.marks) #33
print(s1.college_Name) #ABC College
s1.welcome()
print(s1.getMarks())

s2 = Student("Arjun", 22)
print(s2.name, s2.marks, s2.college_Name) #Arjun 22 ABC College


# class Car:
#     color = 'Blue'
#     model = "Mercedes"

# car1 = Car()
# print(car1.color)
# print(car1.model)