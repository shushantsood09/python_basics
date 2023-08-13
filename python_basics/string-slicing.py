# String slicing works from 0 to n-1.

names = "Shushant,Samay"
print(len(names))
print(names[0 : 5])

fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")
print(fruit[0: 4])  # including 0 but not 4.
print(fruit[:4])
print(fruit[1:4])  # including 1 but not 4.
print(fruit[:])
print(fruit[0:-3])
print(fruit[0:len(fruit)-3])
print(fruit[:len(fruit)-3])
print(fruit[-1:len(fruit)-3])
print(fruit[-3:len(fruit)-1])