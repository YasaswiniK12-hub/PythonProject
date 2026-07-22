# BUILD A TRANSLATOR
# GIRAFFE LANGUAGE
#VOWELS->G
# EXAMPLES
# DOG->DGG
#CAT->CGT
vowels=['a','e','i','o','u','A','E','I','O','U']

def translate(phrase):
    res = ""
    for letter in phrase:
        if letter in vowels:
            res+="g"
        else:
            res+=letter
    return res
print(translate(input("Enter a phrase:")))
# My name -> YASASWINI : YGSGWGNG