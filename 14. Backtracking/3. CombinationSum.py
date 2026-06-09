"""
Combination Sum (Medium)
LeetCode/Source: https://leetcode.com/problems/combination-sum/

Problem:
    Given an array of distinct integers `candidates` and a target integer
    `target`, return all unique combinations of candidates that sum to
    target. The same number may be used an unlimited number of times.
    The solution set must not contain duplicate combinations.

Approach:
    Backtracking: at each step either include the current candidate (and
    stay at the same index, allowing reuse) or move to the next candidate.
    Prune when the remaining target goes below zero.

Time:  O(n^(T/M))  — T = target, M = min candidate; bounded exponential
Space: O(T/M)      — maximum recursion depth
"""

from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """Return all combinations that sum to `target` (elements reusable)."""
    result: List[List[int]] = []
    candidates.sort()  # optional but enables early pruning
    path: List[int] = []

    def backtrack(start: int, remaining: int) -> None:
        if remaining == 0:
            result.append(list(path))
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break  # sorted — no need to check further
            path.append(candidates[i])
            backtrack(i, remaining - candidates[i])  # i (not i+1) → reuse allowed
            path.pop()

    backtrack(0, target)
    return result


if __name__ == "__main__":
    output = combination_sum([2, 3, 6, 7], 7)
    print(f"Combinations for target 7: {output}")
    # Expected: [[2, 2, 3], [7]]

    output2 = combination_sum([2, 3, 5], 8)
    print(f"Combinations for target 8: {output2}")
    # Expected: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

    output3 = combination_sum([2], 1)
    print(f"Combinations for target 1: {output3}")
    # Expected: []  (cannot reach 1 with only 2s)
