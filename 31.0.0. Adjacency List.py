# GraphNode fpr adjacency list
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []
# Or use a hashmap
adjList = {'A': [], 'B': []}

# Given directed edges, build an adjacency list
edges = [['A','B'], ['B','C'], ['C','E'], ['B','E'], ['E','D']]

adjList = {}

for src, dst in edges:
    if src not in adjList:
        adjList[src] = []
    if dst not in adjList:
        adjList[dst] = []
    adjList[src].append(dst)

# count paths (backtracking) DFS is very time consuming O(n ^ v), v is the depth of the decision tree

def dfs(node, target, adjList, visit):
    if node in visit:
        return 0
    if node == target:
        return 1
    
    count = 0
    visit.add(node)
    for neighbor in adjList[node]:
        count += dfs(neighbor, target, adjList, visit)
    visit.remove(node)

    return count

print(dfs('A', 'E', adjList, set()))

# shortest path from node to target
import collections
def bfs(node, target, adjList):
    length = 0
    queue = collections.deque()
    queue.append(node)
    visit = set()
    visit.add(node)

    while queue:
        for _ in range(len(queue)):
            curr = queue.popleft()
            if curr == target:
                return length
            
            for neighbor in adjList[curr]:
                if neighbor not in visit:
                    queue.append(neighbor)
                    visit.add(neighbor)
        length += 1
    return length

print(bfs('A', 'E', adjList)) U（0O