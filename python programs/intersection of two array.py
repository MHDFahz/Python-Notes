a = 1234313
b = 123431
a = sorted(str(a))
b = sorted(str(b))
print(a, "\n", b)
i, j = 0, 0
result = []
print(len(a),len(b))
while i < len(a) and j < len(b):
    if a[i] == b[j]:
        result.append(a[i])
        i += 1
        j += 1
    elif a[i] < b[j]:
        i += 1
    else:
        j += 1
print(result)
