# Merge two sorted linked lists into one sorted list.

# 🔹 Idea (Dummy Node)
# Use a dummy node to simplify logic
# Compare nodes and attach smaller one
# Move pointers forward

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def merge_two_lists(l1, l2):
    dummy = ListNode(-1)
    curr = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next

        curr = curr.next

    # Attach remaining nodes
    if l1:
        curr.next = l1
    if l2:
        curr.next = l2

    return dummy.next

#Time Complexity: O(N + M) where N and M are lengths of l1 and l2
#Space Complexity: O(1)