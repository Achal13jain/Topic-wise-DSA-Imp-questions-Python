"""
Problem: Longest Substring Without Repeating Characters
LeetCode: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Time Complexity: O(n)
Space Complexity: O(min(m, n))
Why optimal: Sliding window with hash set allows checking for duplicates in O(1), expanding and contracting the window efficiently.
"""

# Find the length of the longest substring with all unique characters.
# 🔹 Idea (Sliding Window + HashSet)
# Expand window with right pointer
# If duplicate appears → shrink from left
# Track maximum length


def longest_unique_substring(s):
    left = 0
    max_length = 0
    char_set = set()

    for right in range(len(s)):
        # If character is already in the set, shrink from left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        # Add current character to the set
        char_set.add(s[right])

        # Update maximum length
        max_length = max(max_length, right - left + 1)

    return max_length

# Example usage
s = "abcabcbb"
print(longest_unique_substring(s))  # Output: 3 ("abc")
s = "bbbbb"
print(longest_unique_substring(s))  # Output: 1 ("b")
s = "pwwkew"
print(longest_unique_substring(s))  # Output: 3 ("wke")

# Time Complexity: O(n)
# Space Complexity: O(min(m, n)) where m is the size of the character set and n is the length of the string