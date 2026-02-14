"""
Problem: Middle of the Linked List
LeetCode: https://leetcode.com/problems/middle-of-the-linked-list/

Time Complexity: O(n)
Space Complexity: O(1)
Why optimal: Slow and Fast pointer approach finds the middle in one traversal.
"""

# Return the middle node of a linked list.
# If even length → return second middle.

# 🔹 Idea (Slow & Fast Pointer)
# Slow moves 1 step
# Fast moves 2 steps
# When fast ends → slow is at middle

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def middle_node(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow  # Slow is at middle

#Time Complexity: O(N)
#Space Complexity: O(1)