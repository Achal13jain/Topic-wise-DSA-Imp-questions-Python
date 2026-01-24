# Minimum Size Subarray Sum
# Given an array of positive integers nums and a positive integer target, 
# return the minimal length of a subarray whose sum is greater than or equal to target. 
# If there is no such subarray, return 0 instead.

# Idea 
# 
# Use two pointers to create a sliding window
# Expand the right pointer to increase the sum
# Contract the left pointer to find the minimum length when the sum meets or exceeds the target 


def min_sub_array_len(target, nums):
    n = len(nums)
    min_length = float('inf')
    left = 0
    current_sum = 0

    for right in range(n):
        current_sum += nums[right]

        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return 0 if min_length == float('inf') else min_length

# Example Usage \
print(min_sub_array_len(7,[1,3,4,6,5,2])) # [4,3] -> 2

# ⏱ Time: O(n)
# 📦 Space: O(1)
