# Check if subRoot is a subtree of root.

# 🔹 Idea
# Compare trees at every node
# Use helper isSameTree

def is_same_tree(s, t):
    if not s and not t:
        return True
    if not s or not t:
        return False
    if s.val != t.val:
        return False

    return is_same_tree(s.left, t.left) and is_same_tree(s.right, t.right)

def is_subtree(root, subRoot):
    if not root:
        return False

    if is_same_tree(root, subRoot):
        return True

    return is_subtree(root.left, subRoot) or is_subtree(root.right, subRoot)


# Time Complexity O(n x m)
# Space Complexity O(h)