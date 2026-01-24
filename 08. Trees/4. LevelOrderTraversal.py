# Return nodes level by level.

# 🔹 Idea (BFS)
# Use queue
# Process level-wise

from collections import deque

def level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level = []
        size = len(queue)

        for _ in range(size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result

# Time Complexity: O(n)  
# Space Complexity: O(n)