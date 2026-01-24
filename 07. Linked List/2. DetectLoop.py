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
