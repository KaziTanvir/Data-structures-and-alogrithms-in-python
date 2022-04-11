def fibonacci(n):
    assert n >= 0 and int(n) == n, 'The number has to be integer and positive'
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)




nterms = 15


print("Fibonacci sequence:")
for i in range(nterms):
    term= fibonacci(i)
    a= i+1
    print(f"{a} term is {term}")

