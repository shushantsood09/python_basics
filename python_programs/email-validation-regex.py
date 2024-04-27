# a-z
# 0-9
# . _ time 1
# @ time 1
# . 2 or 3 position from last
import re as r
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_Email = input("Please enter your email address : ")

# Using regex search function.

if r.search(email_condition, user_Email):
    print("Right Email")
else:
    print("Wrong Email")
