# Can perform : +,-,*,/,%
num1=input("Enter a number: ")
num2=input("Enter another number: ")
sign=input("Enter the operation: ")
num1=int(num1)
num2=int(num2)
if sign=="+":
    print(num1+num2)
elif sign=="-":
    print(num1-num2)
elif sign=="*":
    print(num1*num2)
elif sign=="/":
    print(num1/num2)
elif sign=="%":
    print(num1%num2)
else:
    print("Invalid Operator")
# THIS WORKS IN ELSE PART : NUM1> NUM2 . IT EITHER GIVE TRUE OR FALSE