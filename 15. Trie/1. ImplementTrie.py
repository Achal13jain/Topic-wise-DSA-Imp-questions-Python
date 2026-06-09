"""
Implement Trie (Prefix Tree) (Medium)
LeetCode/Source: https://leetcode.com/problems/implement-trie-prefix-tree/

Problem:
    Implement a Trie data structure with three operations:
      - insert(word): Insert a word into the trie.
      - search(word): Return True if the exact word is in the trie.
      - starts_with(prefix): Return True if any inserted word starts
        with the given prefix.

Approach:
    Each node holds a dictionary of child characters and a boolean flag
    marking whether it ends a complete word. insert/search/starts_with
    all walk the trie character by character in O(L).

Time:  O(L) per operation  — L = length of word/prefix
Space: O(L × n)            — n words, each up to L characters
"""

from __future__ import annotations
from typing import Optional


class TrieNode:
    """A single node in the trie."""

    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end: bool = False  # True if a complete word ends here


class Trie:
    """Prefix tree supporting insert, search, and starts_with."""

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert `word` into the trie."""
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        """Return True if `word` exists exactly in the trie."""
        node = self._traverse(word)
        return node is not None and node.is_end

    def starts_with(self, prefix: str) -> bool:
        """Return True if any word in the trie starts with `prefix`."""
        return self._traverse(prefix) is not None

    # ------------------------------------------------------------------
    def _traverse(self, text: str) -> Optional[TrieNode]:
        """Walk the trie following `text`; return the last node or None."""
        node = self.root
        for ch in text:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")

    print(trie.search("apple"))       # Expected: True
    print(trie.search("app"))         # Expected: False
    print(trie.starts_with("app"))    # Expected: True

    trie.insert("app")
    print(trie.search("app"))         # Expected: True

    trie.insert("apply")
    print(trie.starts_with("appl"))   # Expected: True
    print(trie.search("applying"))    # Expected: False

    # Test with completely different prefix
    trie.insert("ball")
    print(trie.starts_with("ban"))    # Expected: False
    print(trie.starts_with("bal"))    # Expected: True
