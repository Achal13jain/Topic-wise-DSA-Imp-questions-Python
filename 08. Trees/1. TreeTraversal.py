"""
Problem: Binary Tree Traversal (Inorder, Preorder, Postorder)
LeetCode: https://leetcode.com/problems/binary-tree-inorder-traversal/

Time Complexity: O(n)
Space Complexity: O(n) (explicit stack and output)
Why optimal: DFS is the standard approach for tree traversals, visiting each node once.
"""

#Traverse a binary tree in different orders.
# Depth-First Search (DFS) can be classified into three main types 
# based on the order in which the nodes are visited
# Orders
# Inorder: Left → Root → Right
# Preorder: Root → Left → Right
# Postorder: Left → Right → Root

def inorder(root):
    result = []
    stack = []
    node = root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        result.append(node.val)
        node = node.right
    return result

def preorder(root):
    if not root:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

def postorder(root):
    if not root:
        return []
    result = []
    stack = [(root, False)]
    while stack:
        node, visited = stack.pop()
        if visited:
            result.append(node.val)
            continue
        stack.append((node, True))
        if node.right:
            stack.append((node.right, False))
        if node.left:
            stack.append((node.left, False))
    return result

# Time Complexity: O(n) 
# Space Complexity: O(n) (explicit stack and output)
