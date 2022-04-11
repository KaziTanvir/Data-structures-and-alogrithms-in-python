import gc
import re


def gcd(a,b):
    assert a==int(a) and b==int(b), 'The numbers must be intergers'
    if a<0:
        a *= -1
    if b<0:
        b *= -1
        
    if b==0:
        return a
    else:
        return gcd(b,a%b)
   
print("The gcd is: ") 
print(gcd(100,10))