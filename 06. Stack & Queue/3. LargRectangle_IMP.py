"""
Problem: Largest Rectangle in Histogram
LeetCode: https://leetcode.com/problems/largest-rectangle-in-histogram/

Time Complexity: O(n)
Space Complexity: O(n)
Why optimal: Monotonic stack finds the nearest smaller element boundaries for each bar in linear time.
"""

# Given heights of histogram bars, find the largest rectangular area.

# Example
# Input:  [2,1,5,6,2,3]
# Output: 10

# 🔹 Idea (Monotonic Stack – VERY IMPORTANT)
# Stack stores indices of increasing heights
# When a smaller height appears:
# Pop from stack
# Calculate area using popped height
# Add a dummy 0 at the end to flush stack


def largest_rectangle_area(heights):
    stack = []      # stack of indices
    max_area = 0
    extended_heights = heights + [0]  # sentinel without mutating caller input

    for i in range(len(extended_heights)):
        # Maintain increasing stack
        while stack and extended_heights[stack[-1]] > extended_heights[i]:
            h = extended_heights[stack.pop()]

            # Width calculation
            if not stack:
                width = i
            else:
                width = i - stack[-1] - 1

            max_area = max(max_area, h * width)

        stack.append(i)

    return max_area
if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3]
    print(largest_rectangle_area(heights))  # Output: 10
# Time Complexity: O(n)
# Space Complexity: O(n)
