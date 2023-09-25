l = [11,45,1,2,3,4,5,1,1,1]
print(l)
l.append(6) 
print(l)
# l.sort()
# print("sorted list : ",l)
# l.sort(reverse=True)
# print("sorted list with reverse : ",l)
# l.reverse()
# print(l)
print(l.index(1))
print(l.count(1))

m = l.copy()
print("List m : ",m)
m[0]= 0
print(m)
print(l)
l.insert(1,889)
print(l)
l.extend(m)
print(l)

k = l + m
print("List k is : ",k)
