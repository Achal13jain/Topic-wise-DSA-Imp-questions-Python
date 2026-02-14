"""
Problem: Container With Most Water
LeetCode: https://leetcode.com/problems/container-with-most-water/

Time Complexity: O(n)
Space Complexity: O(1)
Why optimal: Two Pointer approach greedily maximizes area by moving the shorter line, processing each element once.
"""

# Given an array height where each element represents a vertical line,
# find two lines that together with the x-axis form a container that holds the maximum water.

# Formula
# Area = min(height[left], height[right]) × (right - left)

# Example
# Input:  [1,8,6,2,5,4,8,3,7]
# Output: 49

# 🔹 Idea / Optimal Approach (Two Pointers)
# Key Insight
# Width decreases as pointers move inward
# To maximize area, move the smaller height pointer
# Strategy
# 1. Start with two pointers:
#       left = 0
#       right = n - 1
# 2. Calculate area:
# Move pointer with smaller height
# Keep track of maximum area

def max_area(height):
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        # Calculate width
        width = right - left

        # Height is minimum of two lines
        curr_height = height[left] if height[left] < height[right] else height[right]

        # Calculate area
        area = width * curr_height

        # Update maximum area
        if area > max_water:
            max_water = area

        # Move the pointer pointing to smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water
# Example usage:
heights = [1,8,6,2,5,4,8,3,7]
print(max_area(heights))  # Output: 49  

#Time Complexity: O(n)
#Space Complexity: O(1)