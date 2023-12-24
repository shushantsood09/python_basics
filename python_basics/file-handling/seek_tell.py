with open('seek.txt','r') as f:
    print(type(f))
    #Move to the 10th byte in file.
    f.seek(10)

    # Read the next 5 bytes.
    print(f.tell())
    data = f.read(5)
    print(data)

with open('seek.txt', 'w') as f:
    f.truncate(5)

with open('seek.txt', 'r') as f:
    print(f.read())

