# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curSum):
            if not node:
                return False

            curSum += node.val
            if not node.left and not node.right:
                return curSum == targetSum
            return dfs(node.left, curSum) or dfs(node.right, curSum)

        return dfs(root, 0)


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curSum):
            if not node:
                return False
            curSum += node.val

            if curSum == targetSum and not node.left and not node.right:
                return True
            if dfs(node.left, curSum):
                return True
            if dfs(node.right, curSum):
                return True
            return False

        return dfs(root, 0)


# 本质上get_sum_of_tree就是dfs
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def get_sum_of_tree(root, curSum):
            if root is None:
                return False
            if not root.left and not root.right:
                return curSum + root.val == targetSum
            return get_sum_of_tree(root.left, curSum + root.val) or get_sum_of_tree(
                root.right, curSum + root.val
            )

        return get_sum_of_tree(root, 0)
