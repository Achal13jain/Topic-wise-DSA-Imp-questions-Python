# Convert tree → string → tree back.

# 🔹 Idea (Preorder + Null Markers)

from TreeNode import TreeNode 

def serialize(root):
    result = []

    def dfs(node):
        if not node:
            result.append("#")
            return
        result.append(str(node.val))
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return ",".join(result)

def deserialize(data):
    values = data.split(",")
    index = 0

    def dfs():
        nonlocal index
        if values[index] == "#":
            index += 1
            return None

        node = TreeNode(int(values[index]))
        index += 1
        node.left = dfs()
        node.right = dfs()
        return node

    return dfs()

# Time Complexity O(n)
# Space Complexity O(n)