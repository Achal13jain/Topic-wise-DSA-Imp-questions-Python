# Find the maximum depth of the tree.

# 🔹 Idea
# Height = 1 + max(left height, right height)

def height(root):
    if not root:
        return 0

    left_height = height(root.left)
    right_height = height(root.right)

    return 1 + max(left_height, right_height)
