a = [[0, 2], [5, 10], [13, 23], [24, 25]]
b = [[1, 5], [8, 12], [15, 24], [25, 26]]
lenA = len(a)
lenB = len(b)
A = 0
B = 0
ans = []
while A<=lenA-1 and B<=lenA-1:
    maxs = max(a[A][0], b[B][0])
    mins = min(a[A][1], b[B][1])
    if maxs<=mins:
        ans.append([maxs, mins])
    if(b[B][1] > a[A][1]):
        A += 1
    else:
        B += 1
print(ans)