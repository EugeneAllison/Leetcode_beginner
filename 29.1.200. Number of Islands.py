from typing import Optional, List
from collections import deque, Counter, defaultdict
from bisect import bisect_left, bisect_right
from functools import cache
from itertools import pairwise
import heapq
import collections


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        Rows, Cols = len(grid), len(grid[0])
        visited = set()
        numsOfIslands = 0

        def bfs(r, c):
            queue = collections.deque()
            visited.add((r, c))
            queue.append((r, c))

            while queue:
                r, c = queue.popleft()
                # if change the popleft to pop, then it will be the dfs, of course, the queue will be a stack
                directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

                for dr, dc in directions:
                    if (
                        r + dr in range(Rows)
                        and c + dc in range(Cols)
                        and (r + dr, c + dc) not in visited
                        and grid[r + dr][c + dc] == "1"
                    ):
                        queue.append((r + dr, c + dc))
                        visited.add((r + dr, c + dc))

        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    numsOfIslands += 1

        return numsOfIslands
