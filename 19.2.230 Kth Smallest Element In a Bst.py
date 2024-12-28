# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # iteration traversal solution
        res = []
        stack = []
        cur = root
        # cur拥有root的一切属性

        while cur or stack:
            if (
                cur
            ):  # 使用王卓老师的算法，比旧算法while提升了效率，旧算法是while下面两句，else下面保留。
                stack.append(
                    cur
                )  # 加入了cur 带有val，left和right，是指针压入了栈，不是单纯的数据压入了栈
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right

        return res[k - 1]


# 快一点的方法：
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # iteration traversal solution
        res = []
        stack = []
        cur = root
        # cur拥有root的一切属性
        count = 0

        while cur or stack:
            if (
                cur
            ):  # 使用王卓老师的算法，比旧算法while提升了效率，旧算法是while下面两句，else下面保留。
                stack.append(
                    cur
                )  # 加入了cur 带有val，left和right，是指针压入了栈，不是单纯的数据压入了栈
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                count += 1
                cur = cur.right

            if count == k:
                return res[-1]
