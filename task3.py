#!python3
import json
from task2_test import test1
'''
Ask the user to enter in a list of 5 words.
Convert the word to a string literal JSON object
Write the contents to a file called 'task3.txt'

Example:
Enter a word: frog
Enter a word: french
Enter a word: puppy
Enter a word: escalate
Enter a word: ice

task3.txt contents:
["frog","french","puppy","escalate","ice"]

'''
x=0
words=[]
b= True
filename = 'task3.txt'
file = open(filename,'w')
while b==True:
    tr=input("enter five words=>")
    words.append(tr)
    x=x+1
    if x==5:
        b=False
outputData = json.dumps(words)
file.write(f"{outputData}")
