"""
Word Search (Medium)
LeetCode/Source: https://leetcode.com/problems/word-search/

Problem:
    Given an m×n character grid and a string `word`, return True if the
    word can be constructed from sequentially adjacent cells (horizontally
    or vertically). A cell may not be used more than once per path.

Approach:
    DFS/backtracking from every cell that matches word[0]. Mark cells
    as visited by temporarily changing their character, then restore on
    backtrack. Return True as soon as the word is fully matched.

Time:  O(m × n × 4^L)  — L = word length; 4 directions per cell
Space: O(L)             — recursion stack depth equals word length
"""

from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    """Return True if `word` exists in `board` as a connected path."""
    rows, cols = len(board), len(board[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(r: int, c: int, idx: int) -> bool:
        if idx == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if board[r][c] != word[idx]:
            return False

        temp = board[r][c]
        board[r][c] = "#"  # mark visited

        for dr, dc in directions:
            if dfs(r + dr, c + dc, idx + 1):
                board[r][c] = temp  # restore before returning
                return True

        board[r][c] = temp  # restore
        return False

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False


if __name__ == "__main__":
    board1 = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    print(exist([row[:] for row in board1], "ABCCED"))   # Expected: True
    print(exist([row[:] for row in board1], "SEE"))      # Expected: True
    print(exist([row[:] for row in board1], "ABCB"))     # Expected: False

    board2 = [["a"]]
    print(exist(board2, "a"))   # Expected: True
    print(exist(board2, "b"))   # Expected: False
