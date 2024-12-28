import collections
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = Rows = Cols = len(grid)
        q = collections.deque()
        visited = set()
        q.append((0, 0, 1))
        # we use r, c, length
        visited.add((0, 0))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1),(-1, -1)]
        
        while q:
            r, c, length = q.popleft()
            if min(r, c) < 0 or max(r, c) >= N or grid[r][c] == 1:
                continue
            if r == N - 1 and c == N - 1:
                return length
            for dr, dc in directions:
                if (r + dr, c + dc) not in visited:
                    q.append((r + dr, c + dc, length + 1))
                    visited.add((r + dr, c + dc))
        
        return -1
