# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

        
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                # get min of the right tree
                curr = root.right
                while curr and curr.left:
                    curr = curr.left
                # end
                
                root.val = curr.val
                root.right = self.deleteNode(root.right, curr.val)
        return root