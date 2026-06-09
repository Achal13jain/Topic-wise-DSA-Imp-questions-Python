"""
Unique Paths (Medium)
LeetCode/Source: https://leetcode.com/problems/unique-paths/

Problem:
    A robot is on an m×n grid. It starts at the top-left corner and
    wants to reach the bottom-right corner. It can only move right or
    down at each step. Count how many unique paths exist.

Approach:
    2-D DP: dp[i][j] = number of ways to reach cell (i, j).
    Base case: every cell in the first row or first column has exactly
    1 path. Transition: dp[i][j] = dp[i-1][j] + dp[i][j-1].
    Space-optimised to a single 1-D array.

Time:  O(m × n)
Space: O(n)     — 1-D DP row
"""

from typing import List


def unique_paths(m: int, n: int) -> int:
    """Return the number of unique paths on an m×n grid (space-optimised DP)."""
    # dp[j] = number of ways to reach the current row's column j
    dp = [1] * n  # first row is all 1s

    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]  # dp[j] (from above) + dp[j-1] (from left)

    return dp[n - 1]


def unique_paths_2d(m: int, n: int) -> int:
    """Return unique paths using explicit 2-D DP table (easier to visualise)."""
    dp: List[List[int]] = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]


if __name__ == "__main__":
    print(unique_paths(3, 7))     # Expected: 28
    print(unique_paths(3, 2))     # Expected: 3
    print(unique_paths(1, 1))     # Expected: 1

    # Verify both approaches agree
    for m, n in [(3, 7), (5, 5), (2, 10)]:
        v1 = unique_paths(m, n)
        v2 = unique_paths_2d(m, n)
        print(f"unique_paths({m},{n}) = {v1}  (2D: {v2})  match={v1==v2}")
