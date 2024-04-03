class Student:
    def __init__(self, phy, chem, math):
        self.chem = chem
        self.phy = phy
        self.math = math
        # self.pecentage = str((self.phy + self.chem + self.math)/3) + '%'
        # percentage

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3) + '%'


stu1 = Student(78, 87, 75)
print(stu1.percentage)

stu1.phy = 89
print(stu1.percentage)
