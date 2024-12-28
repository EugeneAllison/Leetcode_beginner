# Quick Select
# 快速选择（Quick Select）是一种用来在无序列表中查找第 k 大或第 k 小元素的算法。它与快速排序（Quick Sort）非常相似，但只关注找到所需的元素，而不需要对整个列表进行排序。


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 作为从小到大排序的索引，原题中的k要倒着数，所以更新一下
        k = len(nums) - k  # 将第 k 大转为第 k 小

        def quickSelect(l, r):
            pivot, p = nums[r], l  # 选择最右边的元素作为枢轴
            for i in range(l, r):  # 遍历从左到右（不包括最右边）
                if nums[i] <= pivot:  # 如果当前元素小于等于枢轴
                    nums[p], nums[i] = nums[i], nums[p]  # 交换元素
                    p += 1  # 移动指针
            nums[p], nums[r] = nums[r], nums[p]  # 最后将枢轴放到正确位置

            if p > k:  # 如果枢轴位置大于k，说明第 k 小元素在左边
                return quickSelect(l, p - 1)  # 在左边区域继续查找
            elif p < k:  # 如果枢轴位置小于k，说明第 k 小元素在右边
                return quickSelect(p + 1, r)  # 在右边区域继续查找
            else:  # 如果 p == k，说明找到了第 k 小元素
                return nums[p]

        return quickSelect(0, len(nums) - 1)  # 从整个数组范围开始查找


import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        for i in range(k - 1):
            heapq.heappop(nums)
        a = heapq.heappop(nums)
        return -a
