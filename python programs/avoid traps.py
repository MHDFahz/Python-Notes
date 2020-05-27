def prime(nums):
    if nums < 2:
        return [1]
    li = []
    for num in range(2, nums + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                li.append(num)
    li.append(1)
    lis = [i for i in li if i <= length]
    return sorted(lis, reverse=True)


N = int(input())
for i in range(N):
    r1, r2 = input().split()
    length = int(input())
    cell = list(input())
    pos = 1
    count = 0
    Success = True
    while(Success):
        temp = prime(pos)
        for j in temp:
            check = 0
            if cell[j] == '#':
                pos += 1
                count += 1
                check = 1
                break
        if check != 1:
            print("No Way")
            Success = False
        if pos == length:
            print(pos, count)
            Success = False
