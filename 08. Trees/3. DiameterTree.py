# Diameter = longest path between any two nodes (may or may not pass through root).

# 🔹 Idea
# Diameter at node = left height + right height
# Track maximum globally

def diameter_of_binary_tree(root):
    diameter = 0

    def dfs(node):
        nonlocal diameter
        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        # Update diameter
        diameter = max(diameter, left + right)

        return 1 + max(left, right)

    dfs(root)
    return diameter

# Time Complexity O(n)
# Space Complexity O(h)