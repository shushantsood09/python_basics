x = 10
print(x) 

def get_Value():
    global x
    x = 5
    print(f'The local x is {x}')

print(f'The global x is {x}')
get_Value()
print(f'The global x is {x}')


