# MAP FUNCTION 
def cube(x):
    return x * x* x

print(cube(9))

l = [1,3,5,6,7,3,3,4]
# newl = []
# for item in l:
#     newl.append(cube(item))
# print(newl)


# Insted to doing the above scenario and putting the loop instead we can put a map function which will do the same work.
# Map is used for the efficiency purposes.

# newl = map(cube, l)
# Convert the above to desired data type. 
# newl = list(map(cube, l))

# We don't need to create a cube function.
# Instead we can use lambda function.
newl = list(map(lambda x: x*x*x, l))
 
print(newl)

# FILTER

def filter_function(a):
    return a > 4

# newnewl = filter(filter_function, l) 
# Convert the above to list.

newnewl = list(filter(filter_function, l)) 
print(newnewl)