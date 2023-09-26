# Tuples are un-changable.
tup = (1)   # return type int
tup = (1, 5, 3,  4, "purple")   # return type tuple
# The below command will not work as we cannot update the tuple as they are un-changeable.
# tup[0] = 20

print(type(tup), tup)
print(tup[0])
print(tup[1])
print(tup[3])

if 3 in tup:
    print("yes, 3 is there!")
else:
    print("no, it is not 3")

# We cannot manupulate tuple either we have to copy it, create a list and then use it for changes.

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)

countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)