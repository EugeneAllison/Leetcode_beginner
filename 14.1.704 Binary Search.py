class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums is None:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            # 注意必须是小于等于，不是小于
            # 如果是小于的话，就要r = m, l = m + 1
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1
