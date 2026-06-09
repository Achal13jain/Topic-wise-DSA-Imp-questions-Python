"""
Top K Frequent Elements (Medium)
LeetCode/Source: https://leetcode.com/problems/top-k-frequent-elements/

Problem:
    Given an integer array `nums` and an integer `k`, return the `k`
    most frequent elements. The answer can be in any order.

Approach:
    Count frequencies with a hash map, then use a max-heap (negate
    counts for Python's min-heap) to extract the top k. Alternatively,
    bucket sort achieves O(n) time.

Time:  O(n log k)  — counting O(n) + k heap pops each O(log n)
Space: O(n)        — frequency map + heap
"""

import heapq
from collections import Counter
from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """Return the k most frequent elements using a max-heap."""
    freq = Counter(nums)
    # negate count to use Python's min-heap as a max-heap
    max_heap = [(-count, num) for num, count in freq.items()]
    heapq.heapify(max_heap)
    return [heapq.heappop(max_heap)[1] for _ in range(k)]


def top_k_frequent_bucket(nums: List[int], k: int) -> List[int]:
    """Return the k most frequent elements using bucket sort — O(n)."""
    freq = Counter(nums)
    # Index = frequency; bucket[i] holds all nums with frequency i
    buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]
    for num, count in freq.items():
        buckets[count].append(num)

    result: List[int] = []
    for i in range(len(buckets) - 1, 0, -1):
        result.extend(buckets[i])
        if len(result) >= k:
            return result[:k]
    return result[:k]


if __name__ == "__main__":
    print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
    # Expected: [1, 2]

    print(top_k_frequent([1], 1))
    # Expected: [1]

    print(top_k_frequent_bucket([1, 1, 1, 2, 2, 3], 2))
    # Expected: [1, 2]

    print(top_k_frequent([4, 4, 4, 6, 6, 7, 7, 7, 7], 2))
    # Expected: [7, 4]
