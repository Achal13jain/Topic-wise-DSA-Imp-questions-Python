"""
Problem: Next Greater Element
LeetCode: https://leetcode.com/problems/next-greater-element-ii/ (Variation: Circular Array usually, here standard array)

Time Complexity: O(n)
Space Complexity: O(n)
Why optimal: Monotonic stack processes each element at most twice (push and pop), ensuring linear time.
"""

# Given an array, for each element, find the next greater element to its right.
# If none exists, return -1.

# Example
# Input:  [4, 5, 2, 25]
# Output: [5, 25, 25, -1]

# 🔹 Idea (Monotonic Stack)
# Use a stack that stores indices
# Traverse from right to left
# Maintain stack in decreasing order
# Stack top gives next greater element

def next_greater_element(arr):
    n = len(arr)
    result = [-1] * n
    stack = []  # stack to store indices

    # Traverse from right to left
    for i in range(n - 1, -1, -1):
        # Remove all elements smaller or equal to current
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()

        # If stack not empty, top is next greater
        if stack:
            result[i] = arr[stack[-1]]

        # Push current index
        stack.append(i)

    return result
# Example usage
arr = [4, 5, 2, 25]
print(next_greater_element(arr))  # Output: [5, 25, 25, -1] 

# Time Complexity: O(n)
# Space Complexity: O(n)