
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
