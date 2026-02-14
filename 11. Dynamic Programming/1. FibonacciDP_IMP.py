"""
Problem: Fibonacci Number
LeetCode: https://leetcode.com/problems/fibonacci-number/

Time Complexity: O(n)
Space Complexity: O(1) (Space Optimized)
Why optimal: Iterative approach avoids recursion stack and processes in linear time with constant space.
"""

# Find the n-th Fibonacci number:
# F(n) = F(n-1) + F(n-2)

# 🔹 DP Idea
# Overlapping subproblems
# Store previous results instead of recomputing

# Fibonacci number Using DP with Space Optimization (This is the most optimal form.)
def fibonacci(n):
    if n <= 1:
        return n

    a = 0  # F(0)
    b = 1  # F(1)

    for _ in range(2, n + 1):
        curr = b + a
        a = b
        b = curr

    return b

# Time Complexity: O(n)
# Space Complexity: O(1)

# DP with Memoization (Top-Down Approach)
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

# Time Complexity: O(n)
# Space Complexity: O(n)

# DP with Tabulation (Bottom-up Approach)
def fib(n):
    if n <= 1:
        return n

    dp = [0] * (n+1)
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

# Time Complexity: O(n)
# Space Complexity: O(n)

# without dp

# def fib(n):
#     a,b=0,1
#     for i in range(n):
#         print(n)
#         a,b=b,a+b

# Time Complexity: O(2ⁿ)