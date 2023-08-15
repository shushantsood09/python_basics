import time

# timeStamp = int(time.strftime('%H:%M:%S'))
# print(timeStamp)
# timeStamp = int(timeStamp)
timeStamp = int(time.strftime('%H'))
print(timeStamp)
# timeStamp = int(time.strftime('%M'))
# print(timeStamp)
# timeStamp = int(time.strftime('%S'))
# print(timeStamp)

if(timeStamp <= 12):
    print("Good Morning People!!")
elif(timeStamp >= 12 and timeStamp <= 16):
    print("Good Afternoon People!!")
elif(timeStamp >= 16 and timeStamp <=21 ):
    print("Good Evening People!!")
else:
    print("Good Night People!!")
