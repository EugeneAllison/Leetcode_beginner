class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            # 递归终点，如果索引i超出数组长度，将当前子集加入结果集
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)  # 递归调用，处理下一个元素

            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)  # 从索引0开始处理
        return res


def subsets(nums):
    res = []  # 用于存储所有的子集

    def backtrack(start, path):
        res.append(path[:])  # 将当前的子集（path）加入结果集（res）中
        for i in range(start, len(nums)):  # 从start索引开始，遍历数组
            path.append(nums[i])  # 选择当前元素，加入子集
            backtrack(i + 1, path)  # 递归调用，生成以当前元素开头的所有子集
            path.pop()  # 回退，移除最后一个元素，尝试其他组合

    backtrack(0, [])  # 从索引0开始，初始子集为空
    return res


# 调用函数并打印结果
print(subsets([1, 2, 3]))

# [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(start, path):
            res.append(path.copy())
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()

        dfs(0, [])
        return res
