print(2**3)
# Inorder to get perform exponent function just use **
def raise_to_power(base, pow):
    if pow==0:
        return 1
    elif pow==1:
        return base
    else:
        res=1
        for i in range(pow):
            res*=base
        return res
print(raise_to_power(2,3))
# you made this mistake remember for i in pow. REMEMBER AN INTEGER OBJECT IS NOT ITERABLE
# WITHOUT LOOP YOU CAN DO IT . RECURSION
