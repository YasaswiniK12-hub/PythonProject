# IF STATEMENTS AND COMPARISONS
# A function taking 3 parameters and returning the maximum among those numbers
# >= comparison operator
def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
print(max_num(2,3,4))
print(max_num(20,8,15))
# >=, !=, <=, ==, >, <.
