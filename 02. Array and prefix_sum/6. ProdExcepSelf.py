"""
Problem: Product of Array Except Self
LeetCode: https://leetcode.com/problems/product-of-array-except-self/

Time Complexity: O(n)
Space Complexity: O(1) (excluding output array)
Why optimal: Uses prefix and suffix products to compute result without division in linear time.
"""

# Product of Array Except Self
# Idea (Prefix and Suffix Products)
# For each index, product of all elements to the left and right

def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    # Prefix products
    left = 1
    for i in range(n):
        result[i] = left
        left *= nums[i]

    # Suffix products
    right = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right
        right *= nums[i]

    return result

# Example usage:
nums = [1, 2, 3, 4]
result = product_except_self(nums)
print(result)  # Output: [24, 12, 8, 6]
# ⏱ Time: O(n)
# 📦 Space: O(1) (output array not counted)