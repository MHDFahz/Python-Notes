import math


def primeFactors(n):
    og = n
    li = []
    while n % 2 == 0:
        li.append(2),
        n = n / 2
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            li.append(i),
            n = n / i
    if n > 2:
        li.append(n)
    li = list(dict.fromkeys(li))
    for i in li:
        if i > M:
            li.pop(li.index(i))
    li = [int(og/x) for x in li]
    return li


def flat(tmp):
    new = []
    for x in tmp:
        for u in x:
            new.append(u)
    new = list(dict.fromkeys(new))
    return new


def common_elements(list1, list2):
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    return result


T = int(input())
for i in range(T):
    ip = list(map(int, input().split()))
    M = ip.pop()
    ans1 = []
    ans2 = []
    ans1.append(primeFactors(ip[0]))
    ans2.append(primeFactors(ip[1]))
    r = True
    l = 0
    count = 0
    while(r):
        tmp = []
        for c in ans1[l]:
            temp = primeFactors(c)
            tmp.append(temp)
        new1 = flat(tmp)
        ans1.append(new1)
        tmp = []
        for c in ans2[l]:
            temp = primeFactors(c)
            tmp.append(temp)
        new2 = flat(tmp)
        ans2.append(new2)
        l += 1
        if new1 == [] and new2 == []:
            r = False
    print(ans1)
    print(ans2)
    print(flat(ans1))
    print(flat(ans2))
    e = common_elements(flat(ans1), flat(ans2))
    if e == []:
        print(-1)
    else:
        p = e[0]
        for b in range(len(ans1)):
            for z in ans1[b]:
                if z == p:
                    count += 1
                    ins = b+1
                    break
            if count > 0:
                break
        count = 0
        for b in range(len(ans2)):
            for z in ans2[b]:
                if z == p:
                    count += 1
                    ins += b+1
                    break
            if count > 0:
                break
        print(p, ins)
