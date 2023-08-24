a = 6
match a:
    case 0:
        print("x is zero")
    case 4: 
        print("x is 4")
    case 5: 
        print("x is 5")
    case _: 
        print("x is",a)


x = 4
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    # Empty case with if-condition
    case _ if x < 10:
        print("x is < 10")
    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _:
        print(x)
    
    
