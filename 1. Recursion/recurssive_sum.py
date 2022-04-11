def sum(n):
    assert n==int(n) , 'The number must be positive integer'
    if n<=0:
        return 0
    else:
        return n+ sum(n-1)
    
print(sum(6))
        