"""
Problem: Search in Rotated Sorted Array
LeetCode: https://leetcode.com/problems/search-in-rotated-sorted-array/

Time Complexity: O(log n)
Space Complexity: O(1)
Why optimal: Modified binary search identifies the sorted half to discard the other half efficiently.
"""

# An originally sorted array is rotated at some pivot.
# Example:
# [4,5,6,7,0,1,2]
# Find the index of target.

# 🔹 Idea
# One half of the array is always sorted
# Identify the sorted half
# Decide whether target lies in that half

def search_rotated(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

# Time Complexity O(log n)
# Space Complexity O(1)