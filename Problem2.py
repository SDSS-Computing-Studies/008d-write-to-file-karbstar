#!python3
import json
"""
Write a program to keep track of your current grades for 8 subjects.  Create a menu system that lets a user do the following:
1. Change the name of their subjects
2. Enter in a new value for their grade
3. Read data from a file
4. Save the current data to a file.
"""
filename = 'corses.txt'
file = open(filename,'r')
data=file.read()
dr=json.loads(data)
filename2 = 'grades.txt'
file2 = open(filename2,'r')
data2=file2.read()
dr2=json.loads(data2)
print("corses")
print(', '.join(dr))
print("grades same order of corses")
print(', '.join(dr2))
x=input("enter what you want to do\na->edit at subjects\nb->edit your grades\n=> ")
if x=='a':
    f=int(input("enter the corse name you want to change from 0-7=>"))
    print(f)
    print(dr[f])
    d=input("what wold you like to replace it with->")
    dr[f]=d
    
    filename3 = 'corses.txt'
    file3 = open(filename,'w')
    outputData = json.dumps(dr)
    file3.write(f"{outputData}")
    print(', '.join(dr2))
elif x=='b':
    f=int(input("enter the grade you want to change from 0-7=>"))
    print(f)
    print(', '.join(dr2))
    d=input("what wold you like to replace it with->")
    dr2[f]=d
    filename4 = 'grades.txt'
    file4 = open(filename4,'w')
    outputData2 = json.dumps(dr2)
    file4.write(f"{outputData2}")
    print(', '.join(dr2))