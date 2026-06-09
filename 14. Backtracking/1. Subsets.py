"""
Subsets (Medium)
LeetCode/Source: https://leetcode.com/problems/subsets/

Problem:
    Given an integer array `nums` with all unique elements, return all
    possible subsets (the power set). The solution set must not contain
    duplicate subsets.

Approach:
    Backtracking: at each step decide to include or skip the current
    element. Recurse with an increasing start index to avoid duplicates.
    When we've considered all elements, record the current path as a
    valid subset.

Time:  O(n × 2^n)  — 2^n subsets, each takes O(n) to copy
Space: O(n)        — recursion depth + current path (result not counted)
"""

from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    """Return all subsets of `nums` (backtracking)."""
    result: List[List[int]] = []
    path: List[int] = []

    def backtrack(start: int) -> None:
        result.append(list(path))  # every prefix is a valid subset
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

    backtrack(0)
    return result


if __name__ == "__main__":
    output = subsets([1, 2, 3])
    print(f"Total subsets: {len(output)}")   # Expected: 8
    for s in sorted(output):
        print(s)
    # Expected (any order): [], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]

    print()
    output2 = subsets([0])
    print(f"Total subsets of [0]: {len(output2)}")  # Expected: 2
    print(output2)  # Expected: [[], [0]]
