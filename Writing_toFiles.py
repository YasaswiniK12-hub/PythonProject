
employee_file=open("employees.txt","w")
#print(employee_file.readline())
employee_file.write("\nFATIMA") # appends at the last
# careful about this n times run n times append
# \n next line appending
employee_file=open("employees1.txt","w")
employee_file.close()
# so yeah "a" appeneds it at the end . "w" overrides the whole file and just writes what you give
# "w" yoiu can create a new file