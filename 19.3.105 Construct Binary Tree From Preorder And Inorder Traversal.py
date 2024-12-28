# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[0:mid])
        # 这里 preorder和 inorder 共同享用一个 mid是因为左根和根的个数总和总是不变的，可以对比着数组一看便知
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        return root
