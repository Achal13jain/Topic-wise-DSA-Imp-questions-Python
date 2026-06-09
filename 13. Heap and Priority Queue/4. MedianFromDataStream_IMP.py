"""
Find Median from Data Stream (Hard)
LeetCode/Source: https://leetcode.com/problems/find-median-from-data-stream/

Problem:
    Design a data structure that supports adding integers from a stream
    and finding the median of all elements added so far. The median is
    the middle element of a sorted sequence (or the average of the two
    middles when the count is even).

Approach:
    Maintain two heaps:
      - `low`  : max-heap of the smaller half (negate values for Python)
      - `high` : min-heap of the larger half
    Invariant: len(low) == len(high) or len(low) == len(high) + 1.
    After each insertion, rebalance so the top of `low` ≤ top of `high`.
    Median = low[0] if odd count, else average of tops.

Time:  O(log n) per addNum  |  O(1) for findMedian
Space: O(n) — stores all numbers
"""

import heapq


class MedianFinder:
    """Stream median finder using two heaps."""

    def __init__(self) -> None:
        self._low: list = []   # max-heap (negated)
        self._high: list = []  # min-heap

    def add_num(self, num: int) -> None:
        """Add an integer from the data stream."""
        # Step 1: push to max-heap (low half)
        heapq.heappush(self._low, -num)

        # Step 2: ensure low's max ≤ high's min
        if self._high and (-self._low[0]) > self._high[0]:
            heapq.heappush(self._high, -heapq.heappop(self._low))

        # Step 3: balance sizes — low may have at most 1 extra
        if len(self._low) > len(self._high) + 1:
            heapq.heappush(self._high, -heapq.heappop(self._low))
        elif len(self._high) > len(self._low):
            heapq.heappush(self._low, -heapq.heappop(self._high))

    def find_median(self) -> float:
        """Return the median of all numbers added so far."""
        if len(self._low) > len(self._high):
            return float(-self._low[0])
        return (-self._low[0] + self._high[0]) / 2.0


if __name__ == "__main__":
    mf = MedianFinder()

    mf.add_num(1)
    mf.add_num(2)
    print(mf.find_median())  # Expected: 1.5

    mf.add_num(3)
    print(mf.find_median())  # Expected: 2.0

    mf2 = MedianFinder()
    for n in [5, 15, 1, 3]:
        mf2.add_num(n)
    print(mf2.find_median())  # Expected: 4.0  (sorted: [1,3,5,15] → (3+5)/2)

    mf3 = MedianFinder()
    mf3.add_num(6)
    print(mf3.find_median())  # Expected: 6.0
