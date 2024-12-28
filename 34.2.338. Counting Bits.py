from typing import Optional, List
from collections import deque, Counter, defaultdict
from bisect import bisect_left, bisect_right
from functools import cache
from itertools import pairwise
import heapq


"""
内置函数（Built-in Function）是指由编程语言本身直接提供的、无需额外导入模块或库即可使用的函数。这些函数通常是语言核心的一部分，具有高效的性能，且能够方便地完成一些常见的任务。

特点
直接可用：无需导入任何库，直接调用即可使用。
高效：由底层优化实现，性能比用户自定义函数更高。
多功能：涵盖数学运算、字符串处理、类型转换等多种功能。
跨平台：内置函数通常在不同的平台上都能一致表现。
Python 中的常见内置函数
以下是一些 Python 常见的内置函数及其用途：

数学运算：

abs(x)：求绝对值。
max(iterable, *args)：返回最大值。
min(iterable, *args)：返回最小值。
sum(iterable)：求和。
类型转换：

int(x)：将值转换为整数。
float(x)：将值转换为浮点数。
str(x)：将值转换为字符串。
字符串处理：

len(s)：计算字符串、列表、元组的长度。
ord(c)：返回字符的 ASCII 值。
bin(x)：将整数转换为二进制字符串。
迭代处理：

enumerate(iterable)：返回可枚举对象，常用于 for 循环。
map(func, iterable)：将函数应用于可迭代对象的每个元素。

"""


# O(n log n)
class Solution:
    def countBits(self, n: int) -> List[int]:
        def countBitNum(num):
            count = 0
            while num:
                if num & 1 == 1:
                    count += 1
                num = num >> 1
            return count

        return [countBitNum(i) for i in range(n + 1)]


# O(n) offset: 补偿；抵消；弥补


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if i & offset == 0:  # or offset * 2 == i, 检查是否为2的幂
                offset = i
            dp[i] = dp[i - offset] + 1
        return dp


# 在动态规划的解法中，offset 表示当前数 i 对应的最大且小于等于 i 的 2 的幂。


# 方法一：逐位检查O(n)
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n + 1):
            one = 0
            for i in range(32):
                if num & (1 << i):
                    one += 1
            res.append(one)
        return res
# 使用 (1 << i) 创建一个仅第 i 位为 1 的掩码. 掩码（英语：Mask）在计算机学科及数字逻辑中指的是一串二进制数字，通过与目标数字的按位操作，达到屏蔽指定位而实现需求。


# 方法二：Brian Kernighan 算法 O(n log n)
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            num = i
            while num != 0:
                res[i] += 1
                num &= num - 1
        return res


# 内置函数O(n log n)
class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bin(i).count("1") for i in range(n + 1)]


# 动态规划（最高位）O(n)
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp


# 动态规划（最低位）O(n)
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp
"""
dp[i >> 1] 表示去掉最低位后的 1 的个数。
(i & 1) 用于判断最低位是否是 1。
"""
