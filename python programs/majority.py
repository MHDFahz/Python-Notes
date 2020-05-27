ar = [2, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5,1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1]
n = len(ar)
dic = {}
for i in ar:
    if i in dic.keys():
        dic[i] = dic[i]+1
    else:
        dic[i] = 1
print(max(dic, key=dic.get))