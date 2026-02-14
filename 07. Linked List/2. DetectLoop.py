"""
Problem: Linked List Cycle
LeetCode: https://leetcode.com/problems/linked-list-cycle/

Time Complexity: O(n)
Space Complexity: O(1)
Why optimal: Floyd's Cycle-Finding Algorithm (Slow & Fast Pointers) detects cycle in linear time with constant space.
"""

# Determine if a linked list has a cycle (loop).

# 🔹 Idea (Slow & Fast Pointer)
# slow moves 1 step
# fast moves 2 steps
# If cycle exists → they will meet

def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True  # Cycle detected

    return False

#Time Complexity: O(N)
#Space Complexity: O(1)
