input = [1, 2, 3, 4]
left = [1]*len(input)
right = [1]*len(input)
result = [1]*len(input)
for i in range(1, len(input)):
    n = abs(i-len(input)+1)
    left[i] = left[i-1]*input[i-1]
    right[n] = right[n+1]*input[n+1]
for i in range(len(left)):
    result[i] = left[i]*right[i]
print(input)
print(result)

