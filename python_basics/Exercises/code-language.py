# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end now append three random characters at the starting and the end else: simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it else: remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

statement = input("Enter the statement")
words = statement.split(' ')
coding = input("Enter 1 for Coding and 2 for decoding")

if(coding):
    nwords = []
    for word in words : 
        if(len(word) >=3):
            r1 = "dgh"
            r2 = "jki"
            statement = statement[1:] + statement[0]
            print(statement)
            statement = r1 + statement[1:] + statement[0] + r2
            nwords.append(statement)
            print(nwords)
        else:
            nwords.append(word[::-1])
        print(" ".join(nwords))
else:
    pass