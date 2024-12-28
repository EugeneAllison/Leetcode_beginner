from typing import Optional, List
from collections import deque, Counter, defaultdict
from bisect import bisect_left, bisect_right
from functools import cache
from itertools import pairwise
import heapq   


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        for i in range(k - 1):
            heapq.heappop(nums)
        a = heapq.heappop(nums)
        return -a


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # quick select code
        k = len(nums) - k


        def quickSearch(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[i], nums[p] = nums[p], nums[i] 
                    p += 1
            
            nums[r], nums[p] = nums[p], nums[r]
            if p > k:
                return quickSearch(l, p - 1)
            elif p < k:
                return quickSearch(p + 1, r)
            else: return nums[p]

        return quickSearch(0, len(nums) - 1)
