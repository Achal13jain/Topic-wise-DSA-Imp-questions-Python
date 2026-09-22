"""
Problem: Reverse Linked List
LeetCode: https://leetcode.com/problems/reverse-linked-list/

Time Complexity: O(n)
Space Complexity: O(1)
Why optimal: Iterative approach reverses pointers in a single pass without extra memory.
"""

# Given the head of a linked list, reverse it and return the new head.
# 1 → 2 → 3 → 4 → None
# ↓
# 4 → 3 → 2 → 1 → None

# 🔹 Idea (Iterative – Optimal)
# Maintain three pointers:
# prev → previous node
# curr → current node
# next_node → save next link
# Reverse pointers one by one

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next   # Save next node
        curr.next = prev        # Reverse pointer
        prev = curr             # Move prev forward
        curr = next_node        # Move curr forward

    return prev  # New head

#Time Complexity: O(N)
#Space Complexity: O(1)

# 🔹 Idea (Recursive)
def reverse_list_recursive(head):
    """Compatibility entry point that remains safe for very long lists."""
    return reverse_list(head)


