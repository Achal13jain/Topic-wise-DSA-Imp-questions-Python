"""
Permutation in String (Medium)
Source: https://leetcode.com/problems/permutation-in-string/

Return True when text contains a permutation of pattern as a substring.

Approach:
    Compare fixed-size frequency tables for pattern and a window of the same
    length in text. Slide the window one character at a time, adding the new
    right character and removing the old left character.

Time Complexity: O(n), where n is the length of text
Space Complexity: O(1), using two 26-character frequency tables
"""


def check_inclusion(pattern: str, text: str) -> bool:
    """Return whether a permutation of lowercase ``pattern`` occurs in ``text``."""
    if len(pattern) > len(text):
        return False
    if not pattern:
        return True
    if any(not "a" <= character <= "z" for character in pattern + text):
        raise ValueError("pattern and text must contain lowercase letters")

    pattern_counts = [0] * 26
    window_counts = [0] * 26
    window_size = len(pattern)

    for index in range(window_size):
        pattern_counts[ord(pattern[index]) - ord("a")] += 1
        window_counts[ord(text[index]) - ord("a")] += 1

    if pattern_counts == window_counts:
        return True

    for right in range(window_size, len(text)):
        window_counts[ord(text[right]) - ord("a")] += 1
        window_counts[ord(text[right - window_size]) - ord("a")] -= 1
        if pattern_counts == window_counts:
            return True

    return False


if __name__ == "__main__":
    assert check_inclusion("ab", "eidbaooo")
    assert not check_inclusion("ab", "eidboaoo")
    assert check_inclusion("adc", "dcda")
    print("All tests passed!")
