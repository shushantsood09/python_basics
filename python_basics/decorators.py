
def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function.")
    return mfx


@greet
def hello():
    print('Hello world')

@greet
def sum(a, b):
    sum = a + b
    print("Total is : ", sum)


# hello()
sum(10, 20)
