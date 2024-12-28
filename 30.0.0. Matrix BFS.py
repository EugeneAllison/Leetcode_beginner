# dfs: O(4^n*m) while bfs: O(n*m)
# 在bfs中，我们关心路径长，而在dfs中，我们关心路径数
import collections
def bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    queue = collections.deque()
    queue.append((0, 0))
    visit.add((0, 0))

    length = 0

    while queue:
        for i in range(len(queue)):
            r, c = queue.popleft()
            if r == ROWS - 1 and c == COLS - 1:
                return length

            neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in neighbors:
                if r + dr < 0 or r + dr >= ROWS or c + dc < 0 or c + dc >= COLS or (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1:
                    continue
                else:
                    visit.add((r + dr, c + dc))
                    queue.append((r + dr, c + dc))

        length += 1

    return -1


grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]
        ]

print(bfs(grid))