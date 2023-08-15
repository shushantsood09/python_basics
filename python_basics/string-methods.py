# Note - The strings are immutable
a = "Shushant!!"
print(len(a))
print(a.upper())
print(a.lower())
#It will strip the trailing characters.
#It will not strip the leading character
print(a.rstrip("!"))

print(a.replace("Shushant","John"))

b = "This is a splitted string."
print(b.split(" "))

blogHeading = 'introduction to pYthon.'
print(blogHeading.capitalize())
print(blogHeading.center(50))
print(len(blogHeading.center(50)))
print(blogHeading.endswith("."))
print(blogHeading.endswith(".", 4, 20))

#We can overrite a variable in python.

str1 = "Welcome to python basics repo."
print(str1.find("too"))  # Gives -1 when supplied pattern is not there


