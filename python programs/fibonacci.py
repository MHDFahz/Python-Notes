def fib():
    a=0
    b=1
    while True:
        yield a
        a,b=b,a+b
for i,j in enumerate(fib()):
    if i > 10:
        break
    print(j)

