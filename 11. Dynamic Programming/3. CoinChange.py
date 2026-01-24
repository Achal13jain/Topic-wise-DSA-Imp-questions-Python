# Given coins and amount, find minimum number of coins to make amount.
# 🔹 DP Idea
# dp[x] = min(dp[x - coin]) + 1
# Try all coins for every amount.

def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

# Time Complexity: O(n × amount)
# Space Complexity: O(amount)