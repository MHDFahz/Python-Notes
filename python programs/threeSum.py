import itertools
def threeSum(list):
    res=[]
    list.sort()
    length=len(list)
    print(list)
    for i in range(length-2):
        if i>0 and list[i]==list[i-1]:
            continue
        l=i+1
        r=length-1
        while l<r:
            total = list[i]+list[l]+list[r]
            if total<0:
                l=l+1
            elif total>0:
                r=r-1
            else:
                res.append([list[i],list[l],list[r]])
                while l<r and list[l]==list[l+1]:
                    l=l+1
                while l<r and list[r]==list[r-1]:
                    r=r-1
                l=l+1
                r=r-1
    return res
print(threeSum([-1,0,1,2,-1,-4]))
list=[-1,0,1,2,-1,-4]
for i in itertools.combinations(list,3):
    if i[0]+i[1]+i[2] == 0:
        print(i)              