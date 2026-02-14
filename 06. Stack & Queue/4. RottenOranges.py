"""
Problem: Rotting Oranges
LeetCode: https://leetcode.com/problems/rotting-oranges/

Time Complexity: O(m * n)
Space Complexity: O(m * n)
Why optimal: Multi-source BFS is the most natural way to simulate the simultaneous spreading in a grid.
"""

# Given a grid:
# 0 → empty
# 1 → fresh orange
# 2 → rotten orange
# Every minute, rotten oranges rot adjacent fresh ones.
# Return minimum time, or -1 if impossible.

# 🔹 Idea (Multi-Source BFS)
# Push all rotten oranges into queue initially
# BFS level-by-level (each level = 1 minute)
# Count fresh oranges
# If fresh remain → return -1

from collections import deque

def oranges_rotting(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0
    time = 0

    # Initialize queue with all rotten oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    # BFS
    while queue and fresh > 0:
        for _ in range(len(queue)):
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Rot fresh orange
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))

        time += 1

    return time if fresh == 0 else -1
# Example usage
grid = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]
print(oranges_rotting(grid))  # Output: 4
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)