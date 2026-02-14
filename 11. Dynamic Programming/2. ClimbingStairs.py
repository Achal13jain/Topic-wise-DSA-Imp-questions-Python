"""
Problem: Climbing Stairs
LeetCode: https://leetcode.com/problems/climbing-stairs/

Time Complexity: O(n)
Space Complexity: O(1)
Why optimal: Reduces to Fibonacci sequence; can be solved iteratively with constant space.
"""

# You can climb 1 or 2 steps.
# In how many distinct ways can you reach the top?
# 🔹 DP Idea
# Same recurrence as Fibonacci:
# dp[i] = dp[i-1] + dp[i-2]

def climb_stairs(n):
    if n <= 2:
        return n

    prev2 = 1
    prev1 = 2

    for _ in range(3, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1


# Time Complexity: O(n)
# Space Complexity: O(1)


def climb_stairs(n):
    if n <= 2:
        return n

    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


# Time Complexity: O(n)
# Space Complexity: O(n)