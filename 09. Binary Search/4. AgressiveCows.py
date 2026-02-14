"""
Problem: Aggressive Cows / Magnetic Force Between Two Balls
LeetCode: https://leetcode.com/problems/magnetic-force-between-two-balls/

Time Complexity: O(n log n) (Sorting) + O(n log(range)) (Binary Search)
Space Complexity: O(1)
Why optimal: Binary search on the answer (distance) checks feasibility in linear time.
"""

# You are given stall positions and k cows.
# Place cows such that minimum distance between any two cows is maximized.

# 🔹 Idea (Binary Search on Distance)
# Sort stall positions
# Minimum distance = 1
# Maximum distance = last − first stall
# Check if cows can be placed with distance ≥ mid

def aggressive_cows(stalls, cows):
    stalls.sort()

    def can_place(distance):
        count = 1
        last_pos = stalls[0]

        for i in range(1, len(stalls)):
            if stalls[i] - last_pos >= distance:
                count += 1
                last_pos = stalls[i]
                if count == cows:
                    return True
        return False

    left = 1
    right = stalls[-1] - stalls[0]
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        if can_place(mid):
            answer = mid
            left = mid + 1   # Try bigger distance
        else:
            right = mid - 1

    return answer

# Time Complexity O(n log n)
# Space Complexity O(1)