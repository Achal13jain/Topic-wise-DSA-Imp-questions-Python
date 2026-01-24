# Given:
# gas[i] = fuel at station i
# cost[i] = fuel needed to reach next station
# Find starting index to complete circular tour.

# 🔹 Greedy Idea
# If total gas < total cost → impossible
# Reset start whenever fuel becomes negative

def gas_station(gas, cost):
    total = 0
    curr = 0
    start = 0

    for i in range(len(gas)):
        total += gas[i] - cost[i]
        curr += gas[i] - cost[i]

        if curr < 0:
            start = i + 1
            curr = 0

    return start if total >= 0 else -1

# Example:
gas=[1,2,3,4,5]
cost=[3,4,5,1,2]
print(gas_station(gas,cost))# Output: 3

# Time Complexity: O(n)
# Space Complexity: O(1)