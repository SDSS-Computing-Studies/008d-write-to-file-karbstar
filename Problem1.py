#!python3
import json
filename = 'task2.txt'
file = open(filename,'r')
data=file.read()
def rf():
    global d
    try:
        f = open("problem1.txt")
        d=True
    except:
        print(1)
        print("File not accessible")
        d=False
rf()
if d==True:
    try: 
        dr=json.load(data)
        t=True
    except:
        print(2)
        print("File not accessible")
        t=False
    if t==True:
        print(dr)
