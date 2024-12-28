from typing import Optional, List
from collections import deque, Counter, defaultdict
from bisect import bisect_left, bisect_right
from functools import cache
from itertools import pairwise
import heapq  # 关于heap的标准包


# 以下是一些常见的heapq库函数：
# heapify(iterable)：将可迭代对象转换为堆结构。
# heappush(heap, x)：将元素x推入堆中。
# heappop(heap)：从堆中弹出并返回最小元素。
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 没有大根堆，所以用取负数的小根堆
        stones = [-s for s in stones]  # 取负数的小根堆
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, x - y)

        return abs(stones[0]) if stones else 0
