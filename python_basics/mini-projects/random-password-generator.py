import random
import string #String module is a collection of string constants.

passwordLength = 12
charValues = string.ascii_letters + string.digits + string.punctuation

# List Comprehension Syntax [function]

password = "".join([random.choice(charValues) for i in range(passwordLength)])
# password = ""
# for i in range(passwordLength):
#     # print(random.choice(charValues))
#     password += random.choice(charValues)

print('Your randomlt generated password string is : ', password)

# value = random.choice([1,2,3,4,5,6,7,8,9])
# value = random.choice(["a", 'b', "c", "d", "e","f"])
# print(value)

# print(type(string.ascii_letters))
# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)

# print(random.choice("Hello"))



