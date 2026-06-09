"""
N-Queens (Hard)
LeetCode/Source: https://leetcode.com/problems/n-queens/

Problem:
    Place n queens on an n×n chessboard such that no two queens attack
    each other (no two share the same row, column, or diagonal). Return
    all distinct solutions as a list of board configurations.

Approach:
    Backtracking row by row: for each row try placing a queen in each
    column. Track occupied columns, forward-diagonals (row-col), and
    backward-diagonals (row+col) in sets for O(1) conflict checks.

Time:  O(n!)   — upper bound; pruning makes it much faster in practice
Space: O(n²)   — board storage + recursion stack
"""

from typing import List


def solve_n_queens(n: int) -> List[List[str]]:
    """Return all valid n-queens board placements."""
    result: List[List[str]] = []
    board = [["."] * n for _ in range(n)]

    cols: set = set()
    diag1: set = set()   # row - col (forward diagonal)
    diag2: set = set()   # row + col (backward diagonal)

    def backtrack(row: int) -> None:
        if row == n:
            result.append(["".join(r) for r in board])
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            # Place queen
            board[row][col] = "Q"
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            backtrack(row + 1)

            # Remove queen (backtrack)
            board[row][col] = "."
            cols.discard(col)
            diag1.discard(row - col)
            diag2.discard(row + col)

    backtrack(0)
    return result


if __name__ == "__main__":
    solutions_4 = solve_n_queens(4)
    print(f"4-Queens: {len(solutions_4)} solution(s)")
    # Expected: 2 solutions
    for sol in solutions_4:
        for row in sol:
            print(row)
        print()

    solutions_1 = solve_n_queens(1)
    print(f"1-Queen:  {len(solutions_1)} solution(s)")
    # Expected: 1 solution  [["Q"]]

    solutions_8 = solve_n_queens(8)
    print(f"8-Queens: {len(solutions_8)} solution(s)")
    # Expected: 92 solutions
