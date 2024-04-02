# class Student:
#     def __init__(self, name, marks1, marks2, marks3):
#         self.name = name
#         self.marks1 = marks1
#         self.marks2 = marks2
#         self.marks3 = marks3

#     def avgMarks(self):
#         avg = (self.marks1 + self.marks2 + self.marks3)/3
#         print("The average marks of", self.name, "are : ", avg)


# s1 = Student("Aman", 86, 67, 74)
# s1.avgMarks()

# Passing Marks as list
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("Hello there!")

    def avgMarks(self):
        avg = 0
        for val in self.marks:
            avg += val
        print("Hi,", self.name, "your average score is", avg/3)


s1 = Student("Aman Singh", [78,89,87])
s1.avgMarks()
print(s1)

s1.name = "IronMan"
s1.avgMarks()
