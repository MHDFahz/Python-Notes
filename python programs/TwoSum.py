def TwoSum(list,target):
    dic = {}
    for i in range(len(list)):
        print(dic)
        if list[i] in dic:
            return dic[list[i]], i
        else:
            dic[target-list[i]] = i


list = [2, 7, 11, 15]
print(TwoSum(list,22))
