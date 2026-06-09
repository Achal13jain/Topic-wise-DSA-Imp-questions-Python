"""
Kth Largest Element in an Array (Medium)
LeetCode/Source: https://leetcode.com/problems/kth-largest-element-in-an-array/

Problem:
    Given an integer array `nums` and an integer `k`, return the k-th
    largest element in the array (not the k-th distinct).

Approach:
    Maintain a min-heap of size k. Iterate through the array: push each
    element and pop the minimum when the heap exceeds k. After processing
    all elements the heap root is the k-th largest.

Time:  O(n log k)  — n pushes, each heap op costs O(log k)
Space: O(k)        — heap holds at most k elements
"""

import heapq
from typing import List


def find_kth_largest(nums: List[int], k: int) -> int:
    """Return the k-th largest element using a min-heap of size k."""
    min_heap: List[int] = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]


def find_kth_largest_sort(nums: List[int], k: int) -> int:
    """Return the k-th largest element using sorting (simpler, O(n log n))."""
    nums.sort(reverse=True)
    return nums[k - 1]


if __name__ == "__main__":
    print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))
    # Expected: 5

    print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
    # Expected: 4

    print(find_kth_largest([1], 1))
    # Expected: 1

    # Verify both approaches agree
    nums = [7, 10, 4, 3, 20, 15]
    k = 3
    print(f"Heap: {find_kth_largest(nums[:], k)}, Sort: {find_kth_largest_sort(nums[:], k)}")
    # Expected: 10  10
