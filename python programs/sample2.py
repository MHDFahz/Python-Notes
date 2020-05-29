def helper(data, k, memo):
    if k == 0:
        return 1
    s = len(data) - k
    if data[s] == '0':
        return 0
    if memo[k] != "null":
        return memo[k]
    result = helper(data, k-1, memo)
    if k >= 2 and int(data[s:s+2]) <= 26:
        result += helper(data, k-2, memo)
    memo[k] = result
    print(memo[k])
    return result


def numways(data):
    memo = [
        "null" for i in range(len(data)+1)]
    print(memo)

    return helper(data, len(data), memo)


data = "12321"
print(data[1])
print(numways(data))
'''
1 2 3 2 1
1 2 3 21
1 23 2 1
1 23 21
12 3 2 1
12 3 21



'''
