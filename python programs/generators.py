def fib():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a+b


for f in fib():
    if f > 50:
        break
    print(f)
for f in fib():
    
