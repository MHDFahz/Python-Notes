num = int(input())
prime = [True for i in range(num+1)]
start = 2
while (start * start <= num):
    if (prime[start] == True):
        for i in range(start*start, num+1, start):
            prime[i] = False
    start += 1
for start in range(2, num):
    if prime[start]:
        print(start)
