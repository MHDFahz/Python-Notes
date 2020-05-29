def group(arr):
    print(arr)
    dic={}
    for word in arr:
        sort="".join(sorted(word))
        if sort not in dic:
            dic[sort]=[word]
        else:
            dic[sort].append(word)
    for k,v in dic.items():
        print(v)
group(['eat','tea','tan','ate','nat','bat'])
