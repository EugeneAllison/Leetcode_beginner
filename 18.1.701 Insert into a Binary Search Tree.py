# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val) 
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        curr = root
        while True:
            if val > curr.val:
                if not curr.right:
                    curr.right = TreeNode(val)
                    return root
                curr = curr.right
            else:
                if not curr.left:
                    curr.left = TreeNode(val)
                    return root
                curr = curr.left

# 我自己想到的方法
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        # root is None 这个补丁非打不可
        prev, curr = root, root
        while curr:
            prev = curr
            if val > curr.val:
                curr = curr.right
            else:
                curr = curr.left
        if val > prev.val:
            prev.right = TreeNode(val)
        else:
            prev.left = TreeNode(val)
        
        return root