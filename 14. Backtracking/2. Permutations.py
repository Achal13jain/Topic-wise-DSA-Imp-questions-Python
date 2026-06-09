"""
Permutations (Medium)
LeetCode/Source: https://leetcode.com/problems/permutations/

Problem:
    Given an array `nums` of distinct integers, return all possible
    permutations in any order.

Approach:
    Backtracking: swap the current element at position `start` with
    every element from `start` to end, then recurse on `start+1`.
    After the recursive call, swap back (backtrack) to restore the
    original order.

Time:  O(n × n!)  — n! permutations, each costs O(n) to copy
Space: O(n)       — recursion depth
"""

from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    """Return all permutations of `nums` using swap-based backtracking."""
    result: List[List[int]] = []

    def backtrack(start: int) -> None:
        if start == len(nums):
            result.append(list(nums))
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]   # choose
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]   # undo

    backtrack(0)
    return result


def permute_path(nums: List[int]) -> List[List[int]]:
    """Alternative: build permutation by tracking a used-set."""
    result: List[List[int]] = []
    path: List[int] = []
    used = [False] * len(nums)

    def backtrack() -> None:
        if len(path) == len(nums):
            result.append(list(path))
            return
        for i, num in enumerate(nums):
            if not used[i]:
                used[i] = True
                path.append(num)
                backtrack()
                path.pop()
                used[i] = False

    backtrack()
    return result


if __name__ == "__main__":
    result = permute([1, 2, 3])
    print(f"Total permutations: {len(result)}")  # Expected: 6
    for p in sorted(result):
        print(p)

    print()
    print("Single element:", permute([1]))
    # Expected: [[1]]

    print("Two elements:", permute([1, 2]))
    # Expected: [[1, 2], [2, 1]]
