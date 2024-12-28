def max_path_sum(triangle, row, col):
    # 如果当前点已经在塔的最底层，返回该点的值
    if row == len(triangle) - 1:
        return triangle[row][col]

    # 递归计算左下方和右下方的最大路径和
    left_sum = max_path_sum(triangle, row + 1, col)
    right_sum = max_path_sum(triangle, row + 1, col + 1)

    # 返回当前点的值加上左右两边较大的路径和
    return triangle[row][col] + max(left_sum, right_sum)


# 示例三角形
triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]

# 计算从塔顶开始的最大路径和
result = max_path_sum(triangle, 0, 0)
print('The longest path of the number tower is:', result)


def max_path_sum(triangle):
    # 获取数字塔的高度
    n = len(triangle)

    # 初始化 DP 数组
    dp = [row[:] for row in triangle]

    # 从倒数第二行开始，逐行向上计算
    for row in range(n - 2, -1, -1):
        for col in range(len(triangle[row])):
            dp[row][col] += max(dp[row + 1][col], dp[row + 1][col + 1])

    # 返回顶点的值，即为最大路径和
    return dp[0][0]


# 示例三角形
triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]

# 计算从塔顶开始的最大路径和
result = max_path_sum(triangle)
print("The longest path of the number tower is:", result)
