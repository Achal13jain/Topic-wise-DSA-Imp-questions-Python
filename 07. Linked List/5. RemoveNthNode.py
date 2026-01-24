# Remove the n-th node from the end in one pass.

# 🔹 Idea (Two Pointers + Dummy)
# Create a gap of n between two pointers
# When fast reaches end, slow is before target

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    slow = dummy
    fast = dummy

    # Move fast n steps ahead
    for _ in range(n):
        fast = fast.next

    # Move both pointers
    while fast.next:
        slow = slow.next
        fast = fast.next

    # Remove nth node
    slow.next = slow.next.next

    return dummy.next

#Time Complexity: O(N)
#Space Complexity: O(1)