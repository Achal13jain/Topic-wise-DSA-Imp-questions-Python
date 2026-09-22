"""
Problem: Path Sum (Variants I, II, III)
LeetCode:
- I: https://leetcode.com/problems/path-sum/
- II: https://leetcode.com/problems/path-sum-ii/
- III: https://leetcode.com/problems/path-sum-iii/

Time Complexity: O(n)
Space Complexity: O(h); Path Sum III also uses an O(h) prefix map.
Why optimal: DFS traverses nodes once; Prefix sum map for III optimizes redundant path checks.
"""

# 🔹 Path Sum I

# Check if root-to-leaf path equals target sum.

def has_path_sum(root, target):
    if not root:
        return False
    stack = [(root, root.val)]
    while stack:
        node, current = stack.pop()
        if not node.left and not node.right and current == target:
            return True
        if node.left:
            stack.append((node.left, current + node.left.val))
        if node.right:
            stack.append((node.right, current + node.right.val))
    return False

# 🔹 Path Sum II

# Return all root-to-leaf paths with given sum.

def path_sum_ii(root, target):
    result = []
    if not root:
        return result
    stack = [(root, root.val, [root.val])]
    while stack:
        node, current, path = stack.pop()
        if not node.left and not node.right and current == target:
            result.append(path)
        if node.right:
            stack.append(
                (node.right, current + node.right.val, path + [node.right.val])
            )
        if node.left:
            stack.append(
                (node.left, current + node.left.val, path + [node.left.val])
            )
    return result

# 🔹 Path Sum III

# Count any downward paths with sum = target.

def path_sum_iii(root, target):
    count = 0
    prefix = {0: 1}
    if not root:
        return 0
    stack = [(root, 0, False)]
    while stack:
        node, parent_sum, exiting = stack.pop()
        current = parent_sum + node.val
        if exiting:
            prefix[current] -= 1
            continue

        count += prefix.get(current - target, 0)
        prefix[current] = prefix.get(current, 0) + 1
        stack.append((node, parent_sum, True))
        if node.right:
            stack.append((node.right, current, False))
        if node.left:
            stack.append((node.left, current, False))
    return count


# ⏱ O(n) 📦 O(n)
