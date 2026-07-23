# Watch out specific errors . Handle it so that it doesn't break the flow
'''
number=int(input("Enter a number: "))
print(number)
print("\n")

'''

'''
# what if instead of entering a number you enter in letter format like "dhbj"
# this thing throws an error: ValueError invalid literal for int() with base 10 
# now let's handle this using try block 
'''

try:
    #value=10/0
    number=int(input("Enter a number:"))
    print(number)
except ZeroDivisionError as err:
    print("Divided by zero")
    print(err) # storing the error in a  variable and printing it
except ValueError:
    print("Invalid Input")
# so you basically put the risky lines of code in the try block. All errors thrown will be handles by except block
# except : too broad except clause. Catches any kind of error
