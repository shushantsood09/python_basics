# Reading a file.

# f = open("myfile.txt", 'r')
# print(f)

# Writing a file. -> It will overwrite the file's content.

f = open("myfile.txt", 'w')
text = f.write("Hey there!")
f.close()
print(f)

# Appending a file. -> It will sppend the file's content.

f = open("myfile.txt", 'a')
text = f.write("Hey there!")
f.close()
print(f)

