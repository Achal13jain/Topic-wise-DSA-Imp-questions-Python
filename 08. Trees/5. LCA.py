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
    if not root:
        return None

    parents = {root: None}
    stack = [root]
    while stack and (p not in parents or q not in parents):
        node = stack.pop()
        if node.left:
            parents[node.left] = node
            stack.append(node.left)
        if node.right:
            parents[node.right] = node
            stack.append(node.right)

    if p not in parents or q not in parents:
        return None

    ancestors = set()
    node = p
    while node is not None:
        ancestors.add(node)
        node = parents[node]

    node = q
    while node not in ancestors:
        node = parents[node]
    return node

# Time Complexity O(n)
# Space Complexity O(h)
