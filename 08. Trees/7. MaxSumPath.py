"""
Problem: Binary Tree Maximum Path Sum
LeetCode: https://leetcode.com/problems/binary-tree-maximum-path-sum/

Time Complexity: O(n)
Space Complexity: O(h)
Why optimal: Computes max contribution of each subtree during a single DFS traversal.
"""

# Find maximum sum path (any nodes, any direction).

# 🔹 Idea
# Ignore negative paths
# Track global max

def max_path_sum(root):
    if not root:
        return 0
    max_sum = float('-inf')
    gains = {None: 0}
    stack = [(root, False)]
    while stack:
        node, visited = stack.pop()
        if visited:
            left = max(gains[node.left], 0)
            right = max(gains[node.right], 0)
            max_sum = max(max_sum, node.val + left + right)
            gains[node] = node.val + max(left, right)
            continue
        stack.append((node, True))
        if node.right:
            stack.append((node.right, False))
        if node.left:
            stack.append((node.left, False))
    return max_sum

# Time Complexity: O(n)
# Space Complexity: O(h)
