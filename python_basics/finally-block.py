def func():
    try:
        l = [1,2,3,4,5]
        i = int(input("Enter a index no : "))
        print(l[i])
        return 1
    except:
        print("some error occoured!")
        return 0
    finally:
        print("I'm always executed")
    print("Im always executed!")

x = func()
print(x)