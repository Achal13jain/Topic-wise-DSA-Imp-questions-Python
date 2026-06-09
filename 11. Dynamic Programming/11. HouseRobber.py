"""
House Robber (Medium)
LeetCode/Source: https://leetcode.com/problems/house-robber/

Problem:
    You are a robber planning to rob houses along a street. Each house
    has a certain amount of money. Adjacent houses have a security
    system — you cannot rob two consecutive houses. Given an array
    `nums` of non-negative integers representing each house's value,
    return the maximum amount you can rob without alerting the police.

Approach:
    Linear DP: at each house decide to rob it (prev_prev + current) or
    skip it (prev). Track only the previous two values to achieve O(1)
    space.

Time:  O(n)
Space: O(1)
"""

from typing import List


def rob(nums: List[int]) -> int:
    """Return the maximum money that can be robbed without adjacent houses."""
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev2 = 0  # best up to house i-2
    prev1 = 0  # best up to house i-1

    for amount in nums:
        current = max(prev1, prev2 + amount)
        prev2 = prev1
        prev1 = current

    return prev1


def rob_tabulation(nums: List[int]) -> int:
    """Same logic using an explicit DP table (easier to see transitions)."""
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]

    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    return dp[n - 1]


if __name__ == "__main__":
    print(rob([1, 2, 3, 1]))      # Expected: 4  (rob house 0 and 2)
    print(rob([2, 7, 9, 3, 1]))   # Expected: 12 (rob house 0, 2, 4)
    print(rob([0]))               # Expected: 0
    print(rob([5, 1, 1, 5]))      # Expected: 10 (rob house 0 and 3)

    # Verify tabulation matches
    for case in [[1, 2, 3, 1], [2, 7, 9, 3, 1], [5, 1, 1, 5]]:
        r1 = rob(case)
        r2 = rob_tabulation(case)
        print(f"rob({case}) = {r1}  (tab: {r2})  match={r1==r2}")
