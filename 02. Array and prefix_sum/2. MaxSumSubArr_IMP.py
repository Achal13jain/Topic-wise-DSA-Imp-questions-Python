"""
Problem: Maximum Subarray Sum (Kadane's Algorithm)
LeetCode: https://leetcode.com/problems/maximum-subarray/

Time Complexity: O(n)
Space Complexity: O(1)
Why optimal: Kadane's Algorithm is the standard linear time solution for this problem.
"""

# The maximum sum of a contiguous subarray.

# 🔹 Idea (Kadane) (sliding window)

# At each index, decide:
# Start new subarray
# Or extend previous one
# Keep track of max sum

def max_subarray(nums):
    max_sum = curr_sum =nums[0]
    
    for i in range(1, len(nums)):
        # Either start new subarray or extend existing one
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(max_sum, curr_sum)

    return max_sum

# Example usage:
nums = [-2,1,-3,4,-1,2,1,-5,4]
result = max_subarray(nums)
print(result)  # Output: 6  # Explanation: [4,-1,2,1] has the largest sum = 6

# ⏱ Time: O(n)
# 📦 Space: O(1)