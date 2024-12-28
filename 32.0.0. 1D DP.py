# brute: 无礼，畜生
# 用decision tree（决策树）来可视化

def bruteForce(n):
    if n <= 1:
        return n
    return bruteForce(n - 1) + bruteForce(n - 2)

# Top-down approach
def memoization(n, cache):
    if n <= 1:
        return n
    if n in cache:
        return cache[n]

    cache[n] = memoization(n - 1, cache) + memoization(n - 2, cache)
    return cache[n]

# 对比以上的代码发现，用cache储存起来用到的数据，降低时间复杂度


# Bottom-up approach: Dynamic Programming
def dp(n):
    if n <= 1:
        return n
    dp = [0, 1]
    i = 2
    while i <= n:
        tmp = dp[1]
        dp[1] = dp[0] + dp[1]
        dp[0] = tmp
        i += 1
    return dp[1]