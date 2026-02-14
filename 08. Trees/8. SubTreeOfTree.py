"""
Problem: Subtree of Another Tree
LeetCode: https://leetcode.com/problems/subtree-of-another-tree/

Time Complexity: O(n * m) (Worst case); can be optimized to O(n+m) via Merkle hashing or serialization.
Space Complexity: O(h)
Why optimal: Standard recursive check is intuitive; advanced linear approaches exist but are complex to implement.
"""

# Check if subRoot is a subtree of root.

# 🔹 Idea
# Compare trees at every node
# Use helper isSameTree

def is_same_tree(s, t):
    if not s and not t:
        return True
    if not s or not t:
        return False
    if s.val != t.val:
        return False

    return is_same_tree(s.left, t.left) and is_same_tree(s.right, t.right)

def is_subtree(root, subRoot):
    if not root:
        return False

    if is_same_tree(root, subRoot):
        return True

    return is_subtree(root.left, subRoot) or is_subtree(root.right, subRoot)


# Time Complexity O(n x m)
# Space Complexity O(h)