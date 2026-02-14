"""
Problem: Path Sum (Variants I, II, III)
LeetCode:
- I: https://leetcode.com/problems/path-sum/
- II: https://leetcode.com/problems/path-sum-ii/
- III: https://leetcode.com/problems/path-sum-iii/

Time Complexity: O(n)
Space Complexity: O(h) (Recursion stack); Path Sum III uses O(h) map space.
Why optimal: DFS traverses nodes once; Prefix sum map for III optimizes redundant path checks.
"""

# 🔹 Path Sum I

# Check if root-to-leaf path equals target sum.

def has_path_sum(root, target):
    if not root:
        return False

    if not root.left and not root.right:
        return target == root.val

    return (has_path_sum(root.left, target - root.val) or
            has_path_sum(root.right, target - root.val))

# 🔹 Path Sum II

# Return all root-to-leaf paths with given sum.

def path_sum_ii(root, target):
    result = []

    def dfs(node, curr_sum, path):
        if not node:
            return

        path.append(node.val)

        if not node.left and not node.right and curr_sum == node.val:
            result.append(path[:])
        else:
            dfs(node.left, curr_sum - node.val, path)
            dfs(node.right, curr_sum - node.val, path)

        path.pop()

    dfs(root, target, [])
    return result

# 🔹 Path Sum III

# Count any downward paths with sum = target.

def path_sum_iii(root, target):
    count = 0
    prefix = {0: 1}

    def dfs(node, curr_sum):
        nonlocal count
        if not node:
            return

        curr_sum += node.val
        count += prefix.get(curr_sum - target, 0)

        prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
        dfs(node.left, curr_sum)
        dfs(node.right, curr_sum)
        prefix[curr_sum] -= 1

    dfs(root, 0)
    return count


# ⏱ O(n) 📦 O(n)