#python3
"""
Have the user enter in their name and email address.
Have the program create a file called 'task1.txt'
Write their name to the first line and their email to the second line.
"""
filename = 'task1.txt'
file = open(filename,'w')
right = input("Enter your name")
file.write(right + "\n")
right = input("Enter your email")
file.write(right + "\n")