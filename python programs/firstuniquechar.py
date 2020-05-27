arr = "abcbcacdassdhsbhz"
dic={}
for i in arr:
    if i in dic.keys():
        dic[i] = dic[i]+1
    else:
        dic[i]=1
for i in arr:
    if dic[i]==1:
        print(i)
        break
