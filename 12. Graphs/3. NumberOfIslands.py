"""
Number of Islands (Medium)
LeetCode/Source: https://leetcode.com/problems/number-of-islands/

Problem:
    Given a 2D grid of '1's (land) and '0's (water), count the number of
    islands. An island is formed by connected '1's (horizontally or
    vertically). You may assume all four edges of the grid are surrounded
    by water.

Approach:
    Iterate over every cell. When a '1' is found, increment the island
    count and flood-fill (DFS) to mark the whole island as visited by
    overwriting its cells with '0'.

Time:  O(m × n)  — each cell is visited at most twice
Space: O(m × n)  — DFS recursion stack in worst case (all land)
"""

from typing import List


def num_islands(grid: List[List[str]]) -> int:
    """Return the count of islands in `grid`."""
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def flood_fill(r: int, c: int) -> None:
        """Mark all connected land cells starting from (r, c) as visited."""
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
            return
        grid[r][c] = "0"          # mark visited
        flood_fill(r + 1, c)
        flood_fill(r - 1, c)
        flood_fill(r, c + 1)
        flood_fill(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                flood_fill(r, c)

    return count


if __name__ == "__main__":
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    print("Islands in grid1:", num_islands(grid1))
    # Expected: 1

    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    print("Islands in grid2:", num_islands(grid2))
    # Expected: 3

    grid3 = [["1"]]
    print("Islands in grid3 (single cell):", num_islands(grid3))
    # Expected: 1
