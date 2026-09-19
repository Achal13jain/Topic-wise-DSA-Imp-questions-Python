"""
Longest Repeating Character Replacement (Medium)
Source: https://leetcode.com/problems/longest-repeating-character-replacement/

Find the longest substring that can be made from one repeated character after
replacing at most k characters.

Approach:
    Maintain a sliding window and the largest character frequency seen in that
    window. The window is valid when its length minus that frequency is at most
    k. Shrink from the left whenever more replacements would be required.

Time Complexity: O(n)
Space Complexity: O(a), where a is the number of distinct characters
"""


def character_replacement(text: str, k: int) -> int:
    """Return the maximum valid repeating-character window length."""
    if k < 0:
        raise ValueError("k must be non-negative")

    frequencies: dict[str, int] = {}
    left = 0
    highest_frequency = 0
    longest = 0

    for right, character in enumerate(text):
        frequencies[character] = frequencies.get(character, 0) + 1
        highest_frequency = max(highest_frequency, frequencies[character])

        while right - left + 1 - highest_frequency > k:
            left_character = text[left]
            frequencies[left_character] -= 1
            left += 1

        longest = max(longest, right - left + 1)

    return longest


if __name__ == "__main__":
    assert character_replacement("ABAB", 2) == 4
    assert character_replacement("AABABBA", 1) == 4
    assert character_replacement("", 1) == 0
    print("All tests passed!")
