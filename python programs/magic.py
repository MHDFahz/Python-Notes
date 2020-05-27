n = int(input())
matrix = []

for i in range(n):
    nums = input()
    matrix.append([int(x) for x in nums.split()])

magic = True
cMatrix = [[] for x in range(n)]
value = sum(matrix[0])
for x, row in enumerate(matrix):
    if sum(row) != value:
        magic = False
    for y, element in enumerate(row):
        cMatrix[y].append(element)
for column in cMatrix:
    if sum(column) != value:
        magic = False
i, j = 0, 0
diagonals = [[], []]
for x in range(n):
    diagonals[0].append(matrix[i][j])
    diagonals[1].append(matrix[n-1-i][j])
    i += 1
    j += 1
if sum(diagonals[0]) != value or sum(diagonals[1]) != value:
    magic = False

if magic == True:
    print('magic')
else:
    print('not magic')
