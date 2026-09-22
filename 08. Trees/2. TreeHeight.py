"""
Problem: Maximum Depth of Binary Tree
LeetCode: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Time Complexity: O(n)
Space Complexity: O(h) (explicit stack for a depth-first traversal)
Why optimal: Simple DFS approach visits every node once to determine maximum depth.
"""

# Find the maximum depth of the tree.

# 🔹 Idea
# Height = 1 + max(left height, right height)

def height(root):
    if not root:
        return 0
    maximum = 0
    stack = [(root, 1)]
    while stack:
        node, depth = stack.pop()
        maximum = max(maximum, depth)
        if node.left:
            stack.append((node.left, depth + 1))
        if node.right:
            stack.append((node.right, depth + 1))
    return maximum
