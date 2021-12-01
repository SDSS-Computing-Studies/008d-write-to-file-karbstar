#!python3
import json

x = 10
y = 3
z = [['Hello','world'], ["Hello","kity"], ["dog","food"]]
print(z[0])
outputData = json.dumps(z)

print(type(z))
print(type(outputData))

file = open('example2.txt','w')
file.write(f"{outputData}")
file.close()

readfile = open('example2.txt','r')
newList = readfile.read()
jsonList = json.loads(newList)
print(type(newList))
print(type(jsonList))
print(jsonList)
print(jsonList[0])


data = [
    {
        "name" : "Joe",
        "type" : "Pikachu"
    },
    {
        "name" : "Bob",
        "type" : "Squirtle"
    }

]
x = json.dumps(data)
print(x)