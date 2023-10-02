dict = {
    "Shushant" : "Software Engineer",
    "spoon" : "Object"
}
print(dict)
print(dict["Shushant"])

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
print(info['name'])
print(info.get('eligible'))
print(info.keys())
print(info.values())

for key in info.keys():
    print(info[key])

print(info.items())
for key,value in info.items():
    print(f'The value corresponding to the key" {key} is {value}')

    