"""
Problem: Fractional Knapsack
LeetCode: N/A (GeeksForGeeks Classic)

Time Complexity: O(n log n)
Space Complexity: O(1)
Why optimal: Taking items with highest value-to-weight ratio first strictly maximizes total value.
"""

# Given items with:
# Value
# Weight
# Knapsack capacity W
# You can take fraction of items.
# Goal:
# Maximize total value.

# 🔹 Greedy Idea
# Take items in descending value/weight ratio
# Always take the most valuable per unit weight first

def fractional_knapsack(items, W):
    # items = [(value, weight)]
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0

    for value, weight in items:
        if W == 0:
            break

        if weight <= W:
            total_value += value
            W -= weight
        else:
            # Take fraction
            total_value += value * (W / weight)
            W = 0

    return total_value

# Time Complexity: O(n log n)
# Space Complexity: O(1)