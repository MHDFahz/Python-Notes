def fre(s):
    dic={}
    res=""
    for i in s:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    print(dic)
    a=sorted(dic,key=lambda x:dic[x],reverse=True)
    for char in a:
        res+=char*dic[char]
    print(res)
fre("Treereet")