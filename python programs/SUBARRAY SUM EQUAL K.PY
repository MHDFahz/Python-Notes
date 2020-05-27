def find(array, k):
    if(len(array) == 0):
        return 0
    currSum = 0
    i = 0
    count = 0
    mymap = []
    while(i < len(array)):
        currSum += array
        if(currSum == k):
            count += 1
        if(mymap.find(currSum-k) != mymap.end()):
            count += mymap[currSum-k]
        mymap[currSum] += 1
        i += 1
    return count


array = [3, 4, 7, 2, -3, 1, 4, 2]
k = 7
print(find(array, k))
