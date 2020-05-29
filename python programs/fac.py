def fib(n=4):
    if n >= 2:
        return n * fib(n-1)
    else:
        return 1


print(fib())
