matrix = [[1, 2, 3,4], [4, 5, 6,6], [7, 8, 9,9],[0,5,3,2]]
for i in matrix:
    print(i)
rb = 0
re = len(matrix)
cb = 0
ce = len(matrix[0])
rs = []
while re > rb and ce > cb:
    for i in range(cb, ce):
        rs.append(matrix[rb][i])
    for j in range(rb+1, re-1):
        print(j)
        rs.append(matrix[j][ce-1])
    if re != rb+1:
        for i in range(ce-1, cb-1, -1):
            rs.append(matrix[re-1][i])
    if cb != ce-1:
        for j in range(re-2, rb, -1):
            rs.append(matrix[j][cb])
    rb += 1
    re -= 1
    cb += 1
    ce -= 1
print(rs)
