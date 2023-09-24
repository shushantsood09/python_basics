
#  Case of required arguments.
def average(a,b):
    print("The average is : ", (a+b)/2)

average(4,6) 

# Case of Default Arguments.
def average(a=9 , b =8):
    print("The average is : ", (a+b)/2)

average(b=10) #It will replace the b default value.

# Taking the arguments as a tuple.
def averageNumbers(*numbers):
    print(type(numbers))
    print(numbers)
    sum =0 
    for i in numbers:
        sum = sum + i
    print("The average of numbers is : ", sum/len(numbers))
    return sum/len(numbers)

averageNumbers(10,20,7)
c = averageNumbers(10,20,70)
print(c)

# Taking the argument as dictionary.
def name(**name):
    print(type(name))
    print(name)
    print("Hello,", name["fname"], name["mname"], name["lname"])
name(mname = "Buchanan", lname = "Barnes", fname = "James")
