# For Loop :
# Can iterate over a sequence of iterable objects in python.
# Iterable obejcts ex => Lists, string;


for i in range(0, 200):
    print(i)


name = "Shushant"
for data in name:
    print(data)


colors = ["Red", "Yellow", "Blue", "Green"]
for color in colors:
    print(color)
    for i in color:
        print(i)


#Range Function -> It is used when we want to iterate it over a sequence.

for i in range(10):
    print(i)


for i in range(1, 10, 2):
    print(i)