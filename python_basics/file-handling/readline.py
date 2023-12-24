# f = open("myfile.txt", 'r')
# while True:
#     line = f.readline()
#     print(line)  
#     if not line:
#         break
#     print(line)

f = open("student_marks", "r")
i = 0 
while True:
    line = f.readline()
    if not line:
        break
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]

    print(f'marks of student {i} in Math is : {m1}')
    print(f'marks of student {i} in Science is : {m2}')
    print(f'marks of student {i} in English is : {m3}')
