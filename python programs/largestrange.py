def largest(array):
    bestrange=[]
    longestlength=0
    nums = {}
    for num in array:
        nums[num] = True
    for num in array:
        if not nums[num]:
            continue
        nums[num] =False
        currentlength = 1
        left= num - 1
        right = num +1
        while left in nums:
            nums[left] = False
            currentlength +=1
            left -=1
        while right in nums:
            nums[right] = False
            currentlength += 1
            right +=1
        if currentlength > longestlength:
            longestlength = currentlength
            bestrange = [left + 1, right - 1]
    return bestrange,nums
print(largest([0,3,2,4,15,16,1,17,11,23,12,13,14,18,19,20,21,44,41,31,21,45,56,78,87,89,99,100,101,102,103,104,105,106,81,82,83,85,86,87,88,90,91,92,30,31,32,34,35,36,37,39,38,40,52,50,51,54,52,55,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,75]))