"""
Problem: 3Sum
LeetCode: https://leetcode.com/problems/3sum/

Time Complexity: O(n^2)
Space Complexity: O(1) (excluding output storage)
Why optimal: Sorting allows us to use the Two Pointer technique, avoiding O(n^3) brute force.
"""

# Given an integer array nums, return all unique triplets
# [nums[i], nums[j], nums[k]] such that:

# nums[i] + nums[j] + nums[k] = 0

# Rules
# Indices must be different
# Triplets must be unique
# Order inside triplet does not matter

# Idea / Optimal Approach (Sorting + Two Pointers)
# Why sorting?
# Helps avoid duplicates
# Allows two-pointer scanning in linear time
# Strategy:
# 1. Sort the array
# 2. Fix one element i
# 3. Use two pointers:
#       left = i + 1
#       right = n - 1
# 4. Move pointers based on sum
# 5. Skip duplicates to avoid repeated triplets

def three_sum(nums):
    nums.sort()               # Sort array
    result = []
    n = len(nums)

    for i in range(n):
        # Skip duplicate elements for first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                # Move both pointers
                left += 1
                right -= 1

                # Skip duplicate second number
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                # Skip duplicate third number
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < 0:
                # Need bigger sum
                left += 1
            else:
                # Need smaller sum
                right -= 1

    return result
# Example usage:
nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]

#Time complexity: O(n^2)
#Space complexity: O(1) (excluding output space)