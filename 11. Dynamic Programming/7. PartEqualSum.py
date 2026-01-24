# Determine if array can be partitioned into two subsets with equal sum.

# 🔹 DP Idea
# Total sum must be even
# Subset sum = total / 2
# Use 1D knapsack

def can_partition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for t in range(target, num - 1, -1):
            dp[t] = dp[t] or dp[t - num]

    return dp[target]


# Time Complexity: O(n × sum) 
# Space Complexity: O(sum)