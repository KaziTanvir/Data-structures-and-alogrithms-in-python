import sys
sys.setrecursionlimit(10000)

def factorial(n):
    assert n >= 0 and int(n), 'Then number must be positive integer only'
    if n in [0,1]:
        return 1
    else:
        return n*factorial(n-1)
 
print("Answer:")
print(factorial(4))