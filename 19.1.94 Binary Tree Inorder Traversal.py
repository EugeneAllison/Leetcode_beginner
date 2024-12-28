# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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

        return res


# 错误代码：
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        result = []
        self.inorderTraversal(root.left)
        # 调用 self.inorderTraversal(root.left) 和 self.inorderTraversal(root.right) 时，结果没有保存到任何变量中。
        # 中序遍历的结果需要合并左子树、根节点、右子树的结果。
        result.append(root.val)
        self.inorderTraversal(root.right)

        return result


# 改正：
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        result.extend(self.inorderTraversal(root.left))  # 递归处理左子树
        result.append(root.val)  # 处理根节点
        result.extend(self.inorderTraversal(root.right))  # 递归处理右子树

        return result


class Solution_2:
    def inorderTraversal(self, root):
        # recursive traversal

        res = []

        def inOrder(root):
            if root is None:
                return
            # 为什么不是 self.inOrder(root.left)
            inOrder(root.left)
            res.append(root.val)
            inOrder(root.right)

        inOrder(root)
        return res


# 下面展示如何应用类
# 示例树
#       1
#        \
#         2
#        /
#       3
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(root)
# 你运行的代码创建了一棵二叉树，并尝试打印根节点 root。然而，打印结果 <__main__.TreeNode object at 0x0000017515124080> 显示的是 TreeNode 对象的内存地址，而不是树的结构或节点的值。这是因为 TreeNode 类没有实现一个自定义的字符串表示方法。默认情况下，Python 打印对象时显示的是对象的类型和内存地址。


# 创建 Solution 实例并调用方法
solution = Solution_2()  # 创建 Solution 类的实例
result = solution.inorderTraversal(root)  # 调用 inorderTraversal 方法
print(result)  # 输出: [1, 3, 2]


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

        return res


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative
        res, stack = [], []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)  # 和下一句话的不要弄得上下颠倒
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res
