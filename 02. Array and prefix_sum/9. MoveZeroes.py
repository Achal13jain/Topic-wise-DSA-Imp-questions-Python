"""
Problem: Move Zeroes
LeetCode: https://leetcode.com/problems/move-zeroes/

Time Complexity: O(n)
Space Complexity: O(1)
Why optimal: Two pointer approach minimizes writes, moving all zeroes to the end in a single pass.
"""

# Move all zeroes to the end of array while maintaining the order of non-zero elements.
# Idea (Two Pointers)
# Use one pointer to track position for non-zero elements.
# Iterate through array, when non-zero found, place it at the tracked position.
# After traversal, fill remaining positions with zeroes.

def move_zeroes(nums):
    pos = 0  # position for next non-zero

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1

# Example usage:
nums = [0, 1, 0, 3, 12]
move_zeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]
# ⏱ Time: O(n)
# 📦 Space: O(1)