"""
Problem: Longest Increasing Subsequence
LeetCode: https://leetcode.com/problems/longest-increasing-subsequence/

Time Complexity: O(n^2) (Implemented); O(n log n) exists (Patience Sorting).
Space Complexity: O(n)
Why optimal: DP approach builds solution by checking all previous elements for each index.
"""

# Longest Increasing Subsequence (LIS)
# 🔹 Problem (Theory)
# Find length of longest strictly increasing subsequence.

# 🔹 DP Idea
# dp[i] = LIS ending at index i
# dp[i] = max(dp[j]) + 1  where j < i and nums[j] < nums[i]

def length_of_LIS(nums):
    n = len(nums)
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Time Complexity: O(n²) 
# Space Complexity: O(n)