# Lambda functions are dingle expressions.

# def double(x):
#     return x*2

# val = double(5)
# print(val)

double = lambda x: x*x
cube = lambda x: x*x*x
avg = lambda x,y: (x+y)/2
print(double(5))
print(cube(5))
print(avg(10,8))