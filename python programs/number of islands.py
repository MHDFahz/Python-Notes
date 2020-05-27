def dfs(grid, i, j, rows, cols):
    if (i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != 1):
        return
    grid[i][j] = 2

    dfs(grid, i+1, j, rows, cols)
    dfs(grid, i, j+1, rows, cols)
    dfs(grid, i-1, j, rows, cols)
    dfs(grid, i, j-1, rows, cols)


grid = [[1, 0, 0,1,0], [1, 0, 1,0,0], [0, 0, 1,0,1], [1, 0, 1,0,1],[1,0,1,1,0]]
rows = (len(grid))
if rows == 0:
    print("0")
cols = len(grid[0])
noi = 0
for i in range(len(grid)):
    for j in range((len(grid[0]))):
        if grid[i][j] == 1:
            dfs(grid, i, j, rows, cols)
            print(grid)
            noi += 1
print(noi)
