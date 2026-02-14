"""
Problem: Find Pivot Index (Equilibrium Index)
LeetCode: https://leetcode.com/problems/find-pivot-index/

Time Complexity: O(n)
Space Complexity: O(1)
Why optimal: Computes total sum first, then iterates once maintaining left_sum and right_sum.
"""

# Given an array of integers, find the Equilibrium Index 
# where the sum of elements on the left equals the sum of elements on the right.
# Idea: Use prefix sums to track left and right sums efficiently.
# Example
# Input:  [-7, 1, 5, 2, -4, 3, 0]
# Output: 3 (index where left sum = right sum)

def equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0

    for i in range(len(arr)):
        right_sum = total_sum - left_sum - arr[i]

        if left_sum == right_sum:
            return i

        left_sum += arr[i]

    return -1  # no equilibrium index
print(equilibrium_index([-7, 1, 5, 2, -4, 3, 0]))  # Output: 3

#Time complexity: O(n)  
# Space complexity: O(1)