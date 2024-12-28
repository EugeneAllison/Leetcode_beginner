# 一个关于回溯算法的题目
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def leafPath(root, path):
    if not root or root.val == 0:
        return False
    path.append(root.val)
    # 加入安排在初始条件之后

    if not root.left and not root.right:
        return True
    if leafPath(root.left, path):
        return True
    if leafPath(root.right, path):
        return True
    path.pop()

    # 回退安排在递归算法之后

    return False


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def buildTree(values):
    if not values:
        return None
    nodes = [None if val is None else TreeNode(val) for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def leafPath(root, path):
    if not root or root.val == 0:
        return False
    path.append(root.val)
    if not root.left and not root.right:
        return True
    if leafPath(root.left, path):
        return True
    if leafPath(root.right, path):
        return True
    path.pop()
    return False


# 构建树
values = [4, 0, 1, None, 7, 3, 2, None, None, None, None, None, 0]
root = buildTree(values)

# 寻找路径
path = []
found = leafPath(root, path)
if found:
    print("Path to a leaf:", path)
else:
    print("No valid path found.")


# -----在回溯算法的几个应用实例中，总是要用到辅助函数（auxiliary functions）dfs，参考习题理解-----
# 这是因为辅助函数可以帮助我们处理一些复杂的逻辑，使主函数更简洁，同时也可以方便递归调用。
# 为什么需要辅助函数：
# 简化逻辑：辅助函数可以将复杂的递归逻辑封装在内部，使主函数更简洁易读。
# 参数管理：辅助函数可以管理递归过程中需要传递的参数。例如，在subsets中，辅助函数backtrack不仅传递了当前的索引start，还传递了当前构建的子集path。
# 状态管理：通过辅助函数，可以更好地管理和恢复递归过程中的状态，避免全局变量的使用。


# 它们的本质确实是实现深度优先搜索（DFS）的逻辑。DFS 是一种遍历或搜索树或图的算法，通常通过递归来实现。在处理组合问题、路径问题或子集问题时，DFS 常常与回溯算法结合使用。

# 辅助函数的本质是DFS
# 在前面的例子中，无论是生成子集还是路径求和，辅助函数的核心都是在执行DFS：

# 生成子集问题中的辅助函数（backtrack）：

# 通过递归遍历数组的每个元素，构建所有可能的子集。
# 每次递归调用都深入一步，将当前元素加入子集，直到遍历完所有元素。
# 路径求和问题中的辅助函数（get_sum_of_tree）：

# 通过递归遍历树的每个节点，计算从根节点到叶子节点的路径和。
# 每次递归调用都深入一步，更新当前路径的和，直到到达叶子节点。
# 这些辅助函数的递归过程正是DFS的过程，通过不断深入树或数组的下一层，实现搜索或遍历的目的。
