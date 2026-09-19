"""
Valid Sudoku (Medium)
Source: https://leetcode.com/problems/valid-sudoku/

Determine whether the filled cells of a 9 x 9 Sudoku board are valid.
Each row, column, and 3 x 3 box must contain no repeated digit.

Approach:
    Track the digits already seen in each row, column, and box. A repeated
    digit in any of the three sets makes the board invalid immediately.

Time Complexity: O(1) for a fixed 9 x 9 board (O(n^2) for an n x n board)
Space Complexity: O(1) for a fixed board
"""


def is_valid_sudoku(board: list[list[str]]) -> bool:
    """Return whether all currently filled Sudoku cells obey the rules."""
    if len(board) != 9 or any(len(row) != 9 for row in board):
        return False

    rows = [set() for _ in range(9)]
    columns = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for row in range(9):
        for column in range(9):
            value = board[row][column]
            if value == ".":
                continue
            if value not in "123456789":
                return False

            box = (row // 3) * 3 + column // 3
            if value in rows[row] or value in columns[column] or value in boxes[box]:
                return False

            rows[row].add(value)
            columns[column].add(value)
            boxes[box].add(value)

    return True


if __name__ == "__main__":
    example = [
        list("53..7...."),
        list("6..195..."),
        list(".98....6."),
        list("8...6...3"),
        list("4..8.3..1"),
        list("7...2...6"),
        list(".6....28."),
        list("...419..5"),
        list("....8..79"),
    ]
    assert is_valid_sudoku(example)
    print("All tests passed!")
