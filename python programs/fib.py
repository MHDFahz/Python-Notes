def fib_2(n, memo,k):
    print(n)
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_2(n-1, memo,"first") + fib_2(n-2, memo,"second")
    print('-')
    memo[n] = result
    return result
n=15
memo=[None for i in range(n+1)]
memo[1],memo[2]=1,1
print(fib_2(n,memo,k=""))
print(memo)