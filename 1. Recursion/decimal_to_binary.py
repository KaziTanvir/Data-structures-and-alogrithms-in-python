def convert(n):
    assert n==int(n), 'The number has to be integer'
    if n==0:
        return 0
    else:
        return n%2 + 10*convert(int(n/2))

print("Converted:")
print(convert(16))