# dms: O(4^n*m) while bms: O(n*m)
# count paths use backtracking
 
def dfs(grid, r, c, visit):
    Rows, Cols = len(grid), len(grid[0])

    if (min(r, c) < 0 or r >= Rows or c >= Cols or (r, c) in visit or grid[r][c] == 1):
        return 0
    if (r == Rows - 1 and c == Cols - 1):
        return 1
    # initial condition: 或者出界（1.最小与2.最大），或者3.已经访问过（图算法中的老三样），或者4.是0（题目中给的特定限制，具体问题具体分析）
    # termination condition: 到达了终点，终止条件

    visit.add((r, c))
    # 紧接着初始条件就是加入set

    count = 0
    count += dfs(grid, r + 1, c, visit)
    count += dfs(grid, r - 1, c, visit)
    count += dfs(grid, r, c + 1, visit)
    count += dfs(grid, r, c - 1, visit)

    visit.remove((r, c))
    return count

grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0]
]

print(dfs(grid, 0, 0, set()))
