"""
Problem: Lowest Common Ancestor of a Binary Tree
LeetCode: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Time Complexity: O(n)
Space Complexity: O(h)
Why optimal: Single pass DFS finds targets and bubbles up the LCA without extra storage.
"""

# Find lowest common ancestor of nodes p and q.

# 🔹 Idea
# If root is p or q, return root
# If both sides return non-null → root is LCA

def lowest_common_ancestor(root, p, q):
    if not root or root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root

    return left if left else right

# Time Complexity O(n)
# Space Complexity O(h)