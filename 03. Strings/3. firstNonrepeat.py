"""
Problem: First Unique Character in a String
LeetCode: https://leetcode.com/problems/first-unique-character-in-a-string/

Time Complexity: O(n)
Space Complexity: O(1) (ASCII size fixed)
Why optimal: Two-pass approach (count freqs then check) is simple and linear.
"""

# First non repeating character in a string
# 🔹 Idea (HashMap + Single Pass)
# Count frequency of each character using a hashmap
# Traverse the string again to find the first character with frequency 1

def first_unique_char(s):
    freq = {}

    # Count frequency
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # Find first non-repeating
    for i in range(len(s)):
        if freq[s[i]] == 1:
            return i

    return -1
# Example usage
s = "leetcode"
print(first_unique_char(s))  # Output: 0 ('l')
s = "loveleetcode"
print(first_unique_char(s))  # Output: 2 ('v')

# Time Complexity: O(n)
# Space Complexity: O(1) (since the character set is fixed - ASCII)