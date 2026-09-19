"""
Design Add and Search Words Data Structure (Medium)
Source: https://leetcode.com/problems/design-add-and-search-words-data-structure/

Store words and support searches in which a dot matches any one character.

Approach:
    Insert words into a trie. Search normally for letters; for a dot, use DFS
    to try every child node at that position.

Time Complexity: O(L) for add; O(L) average search, O(a^L) worst case
Space Complexity: O(total inserted characters)
"""

from __future__ import annotations


class TrieNode:
    """A node containing child characters and an end-of-word marker."""

    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_word = False


class WordDictionary:
    """Trie supporting exact letters and ``.`` wildcard searches."""

    def __init__(self) -> None:
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        """Insert ``word`` into the dictionary."""
        node = self.root
        for character in word:
            node = node.children.setdefault(character, TrieNode())
        node.is_word = True

    def search(self, pattern: str) -> bool:
        """Return whether ``pattern`` matches an inserted word."""

        def dfs(index: int, node: TrieNode) -> bool:
            if index == len(pattern):
                return node.is_word

            character = pattern[index]
            if character == ".":
                return any(dfs(index + 1, child) for child in node.children.values())

            child = node.children.get(character)
            return child is not None and dfs(index + 1, child)

        return dfs(0, self.root)


if __name__ == "__main__":
    dictionary = WordDictionary()
    for value in ("bad", "dad", "mad"):
        dictionary.add_word(value)
    assert not dictionary.search("pad")
    assert dictionary.search(".ad")
    assert dictionary.search("b..")
    print("All tests passed!")
