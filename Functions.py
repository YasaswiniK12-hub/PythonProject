# Bunch of lines of codes that perform a specific task
# organizes code very well
# python sees this keyword ohh ok this person wants to use a function
#The code that goes into the function must be indented
def sayhi():
    print("Hello World!")
print("Top")
sayhi()
print("Bottom")

# let's give a piece of information to the function

def say_name(name, age):
    print("Hello "+name+", you are "+str(age))
say_name("Yugen Quinn",25)

# Let's try something intermediate
# SEND A LIST AND ACCESS ELEMENTS FROM RANGE X TO Y
def print_list(li):
    print(li)
li=[1,2,3,4,5]
print_list(li)