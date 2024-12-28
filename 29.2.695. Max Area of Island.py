class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        Rows, Cols = len(grid), len(grid[0])
        visited = set()

        def dfsArea(r, c):
            # initial condition: 或者出界（1.最小与2.最大），或者3.已经访问过（图算法中的老三样），或者4.是0（题目中给的特定限制，具体问题具体分析）
            if r < 0 or r >= Rows or c < 0 or c >= Cols or (r, c) in visited or grid[r][c] == 0:
                return 0
            # 紧接着初始条件就是加入set
            visited.add((r, c))
            return (
                         1         + 
                 dfsArea(r + 1, c) + 
                 dfsArea(r - 1, c) + 
                 dfsArea(r, c + 1) + 
                 dfsArea(r, c - 1)
            )

        area = 0
        for r in range(Rows):
            for c in range(Cols):
                area = max(area, dfsArea(r, c))

        return area