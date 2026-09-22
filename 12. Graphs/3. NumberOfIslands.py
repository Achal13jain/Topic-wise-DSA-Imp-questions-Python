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
Space: O(m × n)  — explicit stack in the worst case (all land)
"""

from typing import List


def num_islands(grid: List[List[str]]) -> int:
    """Return the count of islands in `grid`."""
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def flood_fill(start_r: int, start_c: int) -> None:
        """Mark connected land without risking a recursion-depth failure."""
        grid[start_r][start_c] = "0"
        stack = [(start_r, start_c)]

        while stack:
            r, c = stack.pop()
            for next_r, next_c in (
                (r + 1, c),
                (r - 1, c),
                (r, c + 1),
                (r, c - 1),
            ):
                if (
                    0 <= next_r < rows
                    and 0 <= next_c < cols
                    and grid[next_r][next_c] == "1"
                ):
                    grid[next_r][next_c] = "0"
                    stack.append((next_r, next_c))

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
