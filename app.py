from math import *

name="Hazel"
age=15
print(f"There once was a girl named "+name)
print(f"She was {age} years old,")
name="Yugen"
age=21
print(f"She loved her name "+name)
print(f"However, she didn't like her age {age} .")
# formatted string : f
#concatenation(+): string to string is valid. Not string to int

print(r"Dead Poet \@ Society")
#without using r I can use backslash literal twice! like this ---> \\@
# raw text: tells python hey just treat the text raw ignore all escaping codes
print("Dead \nPoet\nSociety")

phrase="Digital Diary"
print(phrase)
print(phrase+" is cool!")
# To acquire the information  about strings we have functions
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
# access specific letter with the help of index
print(phrase[3])
# access index with the help of letter
print(phrase.index("Dig"))
print(phrase.replace("Digital","Lovely"))

# Working with Numbers
print(2)
print(2.9087)
print(-23)
print(3+4.5)
print(3*4+5)
print(3*(4+5)) # Handles math operations
#mod operation
print(10%3) # spits out the reminder
num=-5
print(num)
#convert a number into a string
print(str(num)+" my favourite number")
# you wanna  place a number along with a string then this function comes handy : str()
# abs()- absolute value
print(abs(num))
# pow()- power base, exponent
print(pow(4,2))
# max()- maximum number given
print(max(4,6))
# min() -minimum number given
print(min(4,6))
# round()- round a number
print(round(3.14))
# so yeah you have a bunch of math functions . Inorder to use that you have to access it from math library
# at the top you have it go check it
print(floor(3.7))
# floor()- chops of the decimal. Pick the lowest value
print(ceil(3.7))
# ceil()- picks the greatest value
print(sqrt(36))
# sqrt()- square root

