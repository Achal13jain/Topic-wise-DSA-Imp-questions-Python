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
    # Base case: empty list or single node
    if not head or not head.next:
        return head

    # Recurse on the rest of the list
    new_head = reverse_list_recursive(head.next)

    # Reverse the pointers
    head.next.next = head
    head.next = None

    return new_head  # New head


