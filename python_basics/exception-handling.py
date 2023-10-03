a = input("Enter a number : ")
print(f'Multiplication table of {a} is :')

try:
    for i in range(1, 11):
        print(f'{int(a)} * {i} = {int(a) * i}')
except Exception as e:
    print(e)
    print("Sorry some error occoured")


print("Some important lines of code.")
print("End of program")
