from typing import Optional, List
from collections import deque, Counter, defaultdict
from bisect import bisect_left, bisect_right
from functools import cache
from itertools import pairwise
import heapq

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for n in nums:
            if n in hashSet:
                return True
            hashSet.add(n)
        
        return False
