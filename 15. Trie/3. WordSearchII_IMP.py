"""
Word Search II (Hard)
Source: https://leetcode.com/problems/word-search-ii/

Find all dictionary words that can be formed from horizontally or vertically
adjacent board cells without reusing a cell in the same word.

Approach:
    Store all words in a trie, then backtrack from every board cell. Trie
    prefixes stop impossible paths early. Remove found words and exhausted trie
    branches to avoid duplicate work.

Time Complexity: O(m * n * 4^L) worst case
Space Complexity: O(total word characters + L) recursion depth
"""

from __future__ import annotations

from typing import Optional


class TrieNode:
    """A compact trie node used during board traversal."""

    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.word: Optional[str] = None


def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    """Return every unique dictionary word present in ``board``."""
    if not board or not board[0] or not words:
        return []

    root = TrieNode()
    for word in set(words):
        node = root
        for character in word:
            node = node.children.setdefault(character, TrieNode())
        node.word = word

    rows, columns = len(board), len(board[0])
    found: list[str] = []

    def search(row: int, column: int, parent: TrieNode) -> None:
        character = board[row][column]
        node = parent.children.get(character)
        if node is None:
            return

        if node.word is not None:
            found.append(node.word)
            node.word = None

        board[row][column] = "#"
        for next_row, next_column in (
            (row - 1, column),
            (row + 1, column),
            (row, column - 1),
            (row, column + 1),
        ):
            if (
                0 <= next_row < rows
                and 0 <= next_column < columns
                and board[next_row][next_column] != "#"
            ):
                search(next_row, next_column, node)
        board[row][column] = character

        if node.word is None and not node.children:
            del parent.children[character]

    for row in range(rows):
        for column in range(columns):
            search(row, column, root)

    return found


if __name__ == "__main__":
    sample_board = [list("oaan"), list("etae"), list("ihkr"), list("iflv")]
    assert set(find_words(sample_board, ["oath", "pea", "eat", "rain"])) == {
        "eat",
        "oath",
    }
    print("All tests passed!")
