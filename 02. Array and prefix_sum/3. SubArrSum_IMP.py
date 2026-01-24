# Count number of continuous subarrays whose sum equals k

# 🔹 Idea (Prefix Sum + Hashing)

# current_sum - k exists before
# → subarray sum = k

# Use prefix sums to track cumulative sums
# Use a hash map to count occurrences of each prefix sum   

def subarray_sum(nums, k):
    prefix_sum_map = {0: 1}
    curr_sum = 0
    count = 0

    for num in nums:
        curr_sum += num

        # Check if subarray ending here has sum k
        if curr_sum - k in prefix_sum_map:
            count += prefix_sum_map[curr_sum - k]

        # Store prefix sum frequency
        prefix_sum_map[curr_sum] = prefix_sum_map.get(curr_sum, 0) + 1

    return count

# Example usage:
nums = [1, 1, 1]
k = 2
result = subarray_sum(nums, k)
print(result)  # Output: 2  # Explanation: [1,1] occurs twice

# ⏱ Time: O(n)
# 📦 Space: O(n)