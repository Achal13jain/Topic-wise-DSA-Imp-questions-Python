# Given a binary array nums and integer k,
# you may flip at most k zeros to ones.

# Return the maximum number of consecutive 1s.

# 🔹 Idea (Sliding Window)
# Expand window with right
# Count zeros
# If zeros > k → shrink from left
# Track maximum window size

def longest_ones(nums, k):
    left = 0
    zero_count = 0
    max_len = 0

    for right in range(len(nums)):
        # Count zero
        if nums[right] == 0:
            zero_count += 1

        # Shrink window if zeros exceed k
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        # Update maximum length
        max_len = max(max_len, right - left + 1)

    return max_len

# Example usage:
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2   
result = longest_ones(nums, k)
print(result)  # Output: 6

# Time Complexity: O(n)
# Space Complexity: O(1)