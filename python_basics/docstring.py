# Python docstrings are the string literals that appear right after the definition of a function, method, class, or module.
number = int(input("Enter a number : "))

def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)

print(number)
square(number)
print(square.__doc__) #It will print the docsting as well.5
# import this