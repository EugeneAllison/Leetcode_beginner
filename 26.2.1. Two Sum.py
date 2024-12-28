class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}    # {key: n} and {value: index} 每次必须写明白key和value到底是什么
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]   # 内部是key，输出是value，所以一般让value是index
            else: 
                prevMap[n] = i
        
        return