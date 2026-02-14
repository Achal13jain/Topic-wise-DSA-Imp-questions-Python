"""
Problem: Two Sum
LeetCode: https://leetcode.com/problems/two-sum/

Time Complexity: O(n)
Space Complexity: O(n)
Why optimal: Uses a hash map to look up the complement in constant time O(1).
"""

#Two Sum

# Idea (Hashing)

# Traverse array
# For current number x, check if target - x already exists
# Store numbers with their indices

def two_sum(nums, target):
    index_map = {}  # stores number -> index

    for i in range(len(nums)):
        complement = target - nums[i]

        # If complement already seen, we found the answer
        if complement in index_map:
            return [index_map[complement], i]

        # Store current number with index
        index_map[nums[i]] = i

    return []  # return empty if no solution found
# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1]

# ⏱ Time: O(n)
# 📦 Space: O(n)