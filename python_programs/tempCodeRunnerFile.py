
k, j, d = 0, 0, 0
if len(email) >= 6:  #1
    if email[0].isalpha():   #2
        if ("@" in email) and (email.count("@") == 1):    #3
            if (email[-4] == ".") ^ (email[-3] == "."):    #4