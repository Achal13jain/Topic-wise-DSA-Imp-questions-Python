"""
Problem: Find the Duplicate Number
LeetCode: https://leetcode.com/problems/find-the-duplicate-number/

Time Complexity: O(n)
Space Complexity: O(1)
Why optimal: Uses Floyd's Cycle Detection (Tortoise and Hare) to find duplicate in linear time and constant space.
"""

# Array contains n+1 elements with numbers 1 to n.
# Only one number is duplicated.

# 🔹 Idea (Floyd’s Cycle Detection)

# Treat array as linked list.
# Value at each index points to next index.

def find_duplicate(nums):
    slow = nums[0]
    fast = nums[0]

    # Detect cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Find cycle entry
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

# Example usage:
nums = [3,1,3,4,2]
result = find_duplicate(nums)
print(result)  # Output: 3
# ⏱ Time: O(n)
# 📦 Space: O(1)