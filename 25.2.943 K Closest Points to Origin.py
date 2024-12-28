from typing import Optional, List
from collections import deque, Counter, defaultdict
from bisect import bisect_left, bisect_right
from functools import cache
from itertools import pairwise
import heapq  # 关于heap的标准包

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        for x, y in points:
            dist = x**2 + y**2
            minHeap.append([dist, x, y])
            # 在 heapify 过程中，实际上是针对列表中的元素按照第一个元素（也就是距离 dist）进行重新排序，使其满足堆的性质。所以 heapify 的对象是列表中的整个元素，而不是单独的 dist、x 或 y。
        heapq.heapify(minHeap)
        for _ in range(k):
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])

        return res
