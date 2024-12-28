# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for _ in range(qLen):
                node = (
                    q.popleft()
                )  # 存储了节点本身，而非单纯的值，因为接下来还要用到左右的节点等
                # 必须用popleft，用pop的话默认当成stack用途，即使事前定义了queue（deque）也不好使
                if node:  # 非常重要，否则报错：None是没有.left, .val and .right功能的
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res


# 一般性的不计level的层序遍历，输出时一起输出来，内部不再分列表
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            node = q.popleft()
            if node:  # 非常重要，否则报错：None是没有.left, .val and .right功能的
                q.append(node.left)
                q.append(node.right)
                res.append(node.val)

        return res
