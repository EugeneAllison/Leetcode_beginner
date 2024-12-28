# Dynamic Programming


class Solution:
    def climbStairs(self, n: int) -> int:
        prev, now = 1, 1
        for _ in range(n - 1):
            prev, now = now, now + prev
        return now
