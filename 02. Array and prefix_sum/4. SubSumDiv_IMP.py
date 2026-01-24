# Count subarrays whose sum is divisible by k.

# Idea (Prefix Sum % K)

# (prefix_sum % k) repeats
# → difference divisible by k

def subarray_sum_divisible(nums, k):
    prefix_mod_map = {0: 1}  # stores mod value -> count
    curr_sum = 0
    count = 0

    for num in nums:
        curr_sum += num
        mod_value = curr_sum % k

        # Handle negative mod values
        if mod_value < 0:
            mod_value += k

        # If this mod value seen before, add to count
        if mod_value in prefix_mod_map:
            count += prefix_mod_map[mod_value]

        # Store mod value frequency
        prefix_mod_map[mod_value] = prefix_mod_map.get(mod_value, 0) + 1

    return count

# Example usage:
nums = [4,5,0,-2,-3,1]
k = 5
result = subarray_sum_divisible(nums, k)
print(result)  # Output: 7  # Explanation: There are 7 subarrays with sum divisible by 5

# ⏱ Time: O(n)
# 📦 Space: O(n)