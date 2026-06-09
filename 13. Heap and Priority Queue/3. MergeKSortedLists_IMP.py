"""
Merge K Sorted Lists (Hard)
LeetCode/Source: https://leetcode.com/problems/merge-k-sorted-lists/

Problem:
    Given an array of k linked-list heads, each linked list is sorted in
    ascending order. Merge all the linked lists into one sorted linked
    list and return its head.

Approach:
    Use a min-heap of size ≤ k. Initially push the head of each list.
    Each iteration: pop the minimum node, append it to the result, then
    push its next node (if any). The heap ensures we always pick the
    global minimum in O(log k).

Time:  O(n log k)  — n total nodes, each pushed/popped from a heap of size k
Space: O(k)        — heap holds at most k nodes at once
"""

from __future__ import annotations

import heapq
from typing import Optional, List


class ListNode:
    """Singly linked list node."""

    def __init__(self, val: int = 0, next: Optional[ListNode] = None) -> None:
        self.val = val
        self.next = next

    # Allow heap comparison by value
    def __lt__(self, other: ListNode) -> bool:
        return self.val < other.val


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """Merge k sorted linked lists into one sorted list."""
    min_heap: list = []
    for node in lists:
        if node is not None:
            heapq.heappush(min_heap, node)

    dummy = ListNode(0)
    current = dummy

    while min_heap:
        node = heapq.heappop(min_heap)
        current.next = node
        current = current.next
        if node.next:
            heapq.heappush(min_heap, node.next)

    return dummy.next


# ---------------------------------------------------------------------------
# Helper utilities for the demo
# ---------------------------------------------------------------------------

def build_list(values: List[int]) -> Optional[ListNode]:
    """Build a linked list from a Python list of values."""
    dummy = ListNode(0)
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def list_to_python(head: Optional[ListNode]) -> List[int]:
    """Convert linked list to Python list for easy printing."""
    result: List[int] = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    lists1 = [
        build_list([1, 4, 5]),
        build_list([1, 3, 4]),
        build_list([2, 6]),
    ]
    print(list_to_python(merge_k_lists(lists1)))
    # Expected: [1, 1, 2, 3, 4, 4, 5, 6]

    lists2: List[Optional[ListNode]] = []
    print(list_to_python(merge_k_lists(lists2)))
    # Expected: []

    lists3 = [build_list([5])]
    print(list_to_python(merge_k_lists(lists3)))
    # Expected: [5]
