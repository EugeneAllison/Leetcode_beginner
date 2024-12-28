class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canEating(k):
            sumTime = 0
            for pile in piles:
                time = pile // k + 1 if pile % k != 0 else pile // k
                sumTime += time
            return sumTime <= h

        l, r = 1, max(piles)

        while l <= r:
            m = (l + r) // 2
            if canEating(m):
                r = m - 1
            else:
                l = m + 1

        return l


# my solution (Time Limit Exceeded)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 1
        while True:
            sumTime = 0
            for pile in piles:
                time = pile // k + 1 if pile % k != 0 else pile // k
                sumTime += time
            if sumTime <= h:
                return k
            k += 1
