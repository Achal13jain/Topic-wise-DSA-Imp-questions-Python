"""
Problem: Diameter of Binary Tree
LeetCode: https://leetcode.com/problems/diameter-of-binary-tree/

Time Complexity: O(n)
Space Complexity: O(h)
Why optimal: Calculates height and diameter in the same DFS traversal, avoiding repeated work.
"""

# Diameter = longest path between any two nodes (may or may not pass through root).

# 🔹 Idea
# Diameter at node = left height + right height
# Track maximum globally

def diameter_of_binary_tree(root):
    if not root:
        return 0
    diameter = 0
    heights = {None: 0}
    stack = [(root, False)]
    while stack:
        node, visited = stack.pop()
        if visited:
            left = heights[node.left]
            right = heights[node.right]
            diameter = max(diameter, left + right)
            heights[node] = 1 + max(left, right)
            continue
        stack.append((node, True))
        if node.right:
            stack.append((node.right, False))
        if node.left:
            stack.append((node.left, False))
    return diameter

# Time Complexity O(n)
# Space Complexity O(h)
