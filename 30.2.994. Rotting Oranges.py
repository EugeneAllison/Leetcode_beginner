import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        q = collections.deque()
        time, fresh = 0, 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= Rows or nc < 0 or nc >= Cols or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1