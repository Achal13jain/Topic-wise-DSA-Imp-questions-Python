"""
Problem: Edit Distance
LeetCode: https://leetcode.com/problems/edit-distance/

Time Complexity: O(m * n)
Space Complexity: O(m * n)
Why optimal: Standard DP checks all insert/delete/replace possibilities for every prefix pair.
"""

# 🔹 Problem (Theory)
# Convert word1 → word2 using:
# Insert
# Delete
# Replace
# Minimize operations.

# 🔹 DP Idea
# dp[i][j] = min operations to convert
# word1[0:i] → word2[0:j]

def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],     # delete
                    dp[i][j - 1],     # insert
                    dp[i - 1][j - 1]  # replace
                )

    return dp[m][n]

# Time Complexity: O(m × n) 
# Space Complexity: O(m × n)