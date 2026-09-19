"""Behavior tests for the first Core 120 content batch."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path
from types import ModuleType


ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, relative_path: str) -> ModuleType:
    """Load a solution whose filename is not a valid import path."""
    spec = importlib.util.spec_from_file_location(name, ROOT / relative_path)
    if spec is None or spec.loader is None:
        raise ImportError(relative_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


valid_sudoku = load_module("valid_sudoku", "04. Hashing/5. ValidSudoku_IMP.py")
character_replacement = load_module(
    "character_replacement",
    "05. Two pointers & Sliding window/4. CharacterReplacement_IMP.py",
)
permutation_in_string = load_module(
    "permutation_in_string",
    "05. Two pointers & Sliding window/5. PermutationInString.py",
)
word_dictionary = load_module("word_dictionary", "15. Trie/2. AddAndSearchWords_IMP.py")
word_search = load_module("word_search", "15. Trie/3. WordSearchII_IMP.py")


class NewSolutionTests(unittest.TestCase):
    def test_valid_sudoku(self) -> None:
        board = [
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
        self.assertTrue(valid_sudoku.is_valid_sudoku(board))
        board[0][1] = "8"
        self.assertFalse(valid_sudoku.is_valid_sudoku(board))

    def test_character_replacement(self) -> None:
        self.assertEqual(4, character_replacement.character_replacement("AABABBA", 1))
        self.assertEqual(4, character_replacement.character_replacement("ABAB", 2))
        self.assertEqual(0, character_replacement.character_replacement("", 3))

    def test_permutation_in_string(self) -> None:
        self.assertTrue(permutation_in_string.check_inclusion("ab", "eidbaooo"))
        self.assertFalse(permutation_in_string.check_inclusion("ab", "eidboaoo"))
        self.assertTrue(permutation_in_string.check_inclusion("", "anything"))

    def test_word_dictionary_wildcard_search(self) -> None:
        words = word_dictionary.WordDictionary()
        for word in ("bad", "dad", "mad"):
            words.add_word(word)

        self.assertFalse(words.search("pad"))
        self.assertTrue(words.search("bad"))
        self.assertTrue(words.search(".ad"))
        self.assertTrue(words.search("b.."))
        self.assertFalse(words.search(".."))

    def test_word_search_ii_and_board_restoration(self) -> None:
        board = [list("oaan"), list("etae"), list("ihkr"), list("iflv")]
        original = [row[:] for row in board]

        found = word_search.find_words(board, ["oath", "pea", "eat", "rain", "oath"])

        self.assertEqual({"eat", "oath"}, set(found))
        self.assertEqual(original, board)


if __name__ == "__main__":
    unittest.main()
