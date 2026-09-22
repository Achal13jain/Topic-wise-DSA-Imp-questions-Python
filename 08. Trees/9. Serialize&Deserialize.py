"""
Problem: Serialize and Deserialize Binary Tree
LeetCode: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Time Complexity: O(n)
Space Complexity: O(n)
Why optimal: Preorder traversal with null markers uniquely reconstructs the tree in linear time.
"""

# Convert tree → string → tree back.

# 🔹 Idea (Preorder + Null Markers)

from TreeNode import TreeNode 

def serialize(root):
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        if not node:
            result.append("#")
            continue
        result.append(str(node.val))
        stack.append(node.right)
        stack.append(node.left)
    return ",".join(result)

def deserialize(data):
    if not data or data == "#":
        return None
    values = data.split(",")
    root = TreeNode(int(values[0]))
    stack = [(root, 0)]  # state 0 expects left; state 1 expects right

    for value in values[1:]:
        parent, state = stack[-1]
        child = None if value == "#" else TreeNode(int(value))

        if state == 0:
            parent.left = child
            stack[-1] = (parent, 1)
        else:
            parent.right = child
            stack.pop()

        if child:
            stack.append((child, 0))

    return root

# Time Complexity O(n)
# Space Complexity O(n)
