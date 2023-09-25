l = [2,2,3, "Shushant", True]
print(l)
print(type(l))
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])
# print(l[5])  Out of range error.

print(l[-3])  # Negative Index
print(l[len(l)-3])  # Positive Index

if "Shushant" in l:
    print("Yes")
else:
    print("No")
    
# Same thing applies for strings as well.
if "hush" in "Shushant":
    print("Yes")
else:
    print("No")

print(l)
print(l[:])
print(l[1:-1])
print(l[1:4])
print(l[1:4:2])

