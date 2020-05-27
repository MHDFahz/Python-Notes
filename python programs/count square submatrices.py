grid = [[0, 0, 1, 0], [0, 1, 1, 0], [1, 1, 1, 1]]
for i in grid:
    print(i)
rows = (len(grid))
if rows == 0:
    print("0")
cols = len(grid[0])
grid2 = []
count = 0
print()
for i in range(rows):
    ls = []
    for j in range(cols):
        ls.append(0)
        if i == 0:
            ls[j] = grid[i][j]
        if j == 0:
            ls[0] = grid[i][0]
        count += ls[j]
    grid2.append(ls)
for i in range(1, rows):
    for j in range(1, cols):
        if grid[i][j] == 1:
            grid2[i][j] = 1 + \
                min(grid2[i-1][j], min(grid2[i-1][j-1], grid2[i][j-1]))
            count += grid2[i][j]
for i in grid2:
    print(i)
print(count)
