"""
Problem: Maximum Product Subarray
LeetCode: https://leetcode.com/problems/maximum-product-subarray/

Time Complexity: O(n)
Space Complexity: O(1)
Why optimal: Tracks min and max products at each step to handle negative numbers in one pass.
"""

# Find maximum product of a contiguous subarray.

# 🔹 DP Idea
# Negative × negative = positive
# Track both max and min product

def max_product(nums):
    max_prod = nums[0]
    min_prod = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        curr = nums[i]

        temp_max = max(curr, max_prod * curr, min_prod * curr)
        min_prod = min(curr, max_prod * curr, min_prod * curr)
        max_prod = temp_max

        result = max(result, max_prod)

    return result

# Time Complexity: O(n) 
# Space Complexity: O(1)