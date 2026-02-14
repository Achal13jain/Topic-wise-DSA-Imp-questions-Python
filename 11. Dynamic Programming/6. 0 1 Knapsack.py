"""
Problem: 0/1 Knapsack Problem
LeetCode: N/A (GeeksForGeeks Classic)

Time Complexity: O(n * W)
Space Complexity: O(n * W)
Why optimal: Standard DP approach solves subproblems for every item and capacity combination.
"""

# Each item can be taken once or not taken.
# Maximize value under weight constraint.

# 🔹 DP Idea
# dp[i][w] = max value using first i items with capacity w

def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

# Time Complexity: O(n × W)
# Space Complexity: O(n × W)