li = list(map(int, input().split()))
sum = int(input())
cs, d = 0, {}
for i in range(len(li)):
    cs += li[i]
    if cs == sum:
        print(li[0:i+1])
        break
    if cs-sum in d:
        print(li[d[cs-sum]+1:i+1])
        break
    d[cs] = i
else:
    print("not found")
