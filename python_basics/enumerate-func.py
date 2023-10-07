marks = [56, 67, 88, 78, 98, 67, 78, 90, 98, 90]

# index = 0

# for mark in marks:
#     print(mark)
#     if (index == 4):
#         print("Shushant Awesome!")
#     index+=1

for index, mark in enumerate(marks):
    print(mark)
    if (index == 4):
        print("Shushant Awesome!")


# Loop over a list and print the index and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit)
