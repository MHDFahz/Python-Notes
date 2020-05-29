dic={'I':1,'V':5,'X':10,"L":50,'C':100,'D':500,'M':1000}
num=''
pre=0
cur=0
total=0
print(len(num))
for i in range(len(num)):
    cur=dic[num[i]]
    print(cur,pre)
    if cur>pre:
        total = total+cur - 2* pre
    else:
        total += cur
    pre = cur
print(total)