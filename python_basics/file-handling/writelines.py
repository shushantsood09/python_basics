f = open("writelines.txt",'w')
lines = ['Hey there!\n', 'line 2 \n' ]
f.writelines(lines)
f.close()