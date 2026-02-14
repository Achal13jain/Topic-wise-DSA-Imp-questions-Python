"""
Problem: Sliding Window Maximum
LeetCode: https://leetcode.com/problems/sliding-window-maximum/

Time Complexity: O(n)
Space Complexity: O(k)
Why optimal: Monotonic Deque ensures we only store useful indices, allowing O(1) checking of maximum.
"""

# Given an array nums and window size k,
# return the maximum element in each sliding window.
# Example
# nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output = [3,3,5,5,6,7]

# 🔹 Idea (Monotonic Deque)
# Maintain a deque of indices of elements in the current window
# Deque is always in decreasing order of values
# Front of deque = maximum of window

from collections import deque

def sliding_window_max(nums, k):
    dq = deque()   # stores indices
    result = []

    for i in range(len(nums)):
        # Remove indices outside current window
        if dq and dq[0] == i - k:
            dq.popleft()

        # Remove smaller elements (they can't be max)
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        # Add current index
        dq.append(i)

        # Window starts when i >= k - 1
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
# Example usage:
nums = [1,3,-1,-3,5,3,6,7]
k = 3
result = sliding_window_max(nums, k)
print(result)  # Output: [3,3,5,5,6,7]
# Time Complexity: O(n)
# Space Complexity: O(k)