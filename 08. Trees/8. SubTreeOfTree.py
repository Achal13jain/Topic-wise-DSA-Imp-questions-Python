"""
Problem: Subtree of Another Tree
LeetCode: https://leetcode.com/problems/subtree-of-another-tree/

Time Complexity: O(n * m) (Worst case); can be optimized to O(n+m) via Merkle hashing or serialization.
Space Complexity: O(h)
Why optimal: Explicit stacks avoid recursion-depth failures while comparing each candidate subtree.
"""

# Check if subRoot is a subtree of root.

# 🔹 Idea
# Compare trees at every node
# Use helper isSameTree

def is_same_tree(s, t):
    stack = [(s, t)]
    while stack:
        first, second = stack.pop()
        if not first and not second:
            continue
        if not first or not second or first.val != second.val:
            return False
        stack.append((first.left, second.left))
        stack.append((first.right, second.right))
    return True

def is_subtree(root, subRoot):
    if not subRoot:
        return True
    if not root:
        return False
    stack = [root]
    while stack:
        node = stack.pop()
        if node.val == subRoot.val and is_same_tree(node, subRoot):
            return True
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return False


# Time Complexity O(n x m)
# Space Complexity O(h)
