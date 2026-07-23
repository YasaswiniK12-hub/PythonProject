# you want to read info from text file , csv files. How do we do it ?
# We use something called python read command
# reading, opening files
# file can be relative path, absolute path or jsut the file's name if both the files are in the same directory
employee_file=open("employees.txt","r")
# "r": read mode
# "w": write mode ( change the file , modify , add)
# "a":append mode ( you  cannot modify the info in the file but ypu can add
# "r+": read and write

# after you open it, it is important to check whether the file you've opened is readable or not. We get a boolean value
print(employee_file.readable())
#print(employee_file.read()) # spits out all the information
print(employee_file.readline()) # reading the first line in the file
#print(employee_file.readlines()) # puts everything into array
for employee in employee_file.readlines():
    print(employee)
'''
# why can't you see boyd again because read makes the cursor move from start to end.
 Now your'e again saying readline the very first line look at the cursor at the end nothing's after that.
'''


employee_file.close()
# when you open a file you must close the file too
