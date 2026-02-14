"""
Problem: Maximum Depth of Binary Tree
LeetCode: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Time Complexity: O(n)
Space Complexity: O(h) (recursion stack)
Why optimal: Simple DFS approach visits every node once to determine maximum depth.
"""

# Find the maximum depth of the tree.

# 🔹 Idea
# Height = 1 + max(left height, right height)

def height(root):
    if not root:
        return 0

    left_height = height(root.left)
    right_height = height(root.right)

    return 1 + max(left_height, right_height)
