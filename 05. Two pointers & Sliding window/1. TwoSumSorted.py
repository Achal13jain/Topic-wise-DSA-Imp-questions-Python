# You are given a sorted array nums and a target.
# Find 1-based indices of two numbers such that:
# nums[i] + nums[j] = target
# 👉 Exactly one solution exists.
# 🔹 Idea (Two Pointers)
# Use two pointers:
# left at start
# right at end
# If sum is:
# Too small → move left
# Too large → move right


def two_sum_sorted(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        curr_sum = nums[left] + nums[right]

        if curr_sum == target:
            # Return 1-based indices
            return [left + 1, right + 1]
        elif curr_sum < target:
            # Need bigger sum
            left += 1
        else:
            # Need smaller sum
            right -= 1
    return []  # Just for safety, though problem guarantees one solution

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum_sorted(nums, target)
print(result)  # Output: [1, 2]
# Time Complexity: O(n)
# Space Complexity: O(1)