"""
Problem: Longest Palindromic Substring
LeetCode: https://leetcode.com/problems/longest-palindromic-substring/

Time Complexity: O(n^2)
Space Complexity: O(1)
Why optimal: Expand Around Center approach uses constant space compared to O(n^2) DP table.
"""

# Return the longest substring that is a palindrome.
# 🔹 Idea (Expand Around Center)
# Each index is a center
# Expand for odd & even length palindromes

def longest_palindrome(s):
    # Helper function to expand around center
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    start = 0 # Starting index of longest palindrome
    end = 0 # Ending index of longest palindrome

    # Check each index as center
    
    for i in range(len(s)):
        len1 = expand(i, i)       # Odd length
        len2 = expand(i, i + 1)   # Even length
        max_len = max(len1, len2)

        # Update start and end if longer palindrome found
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end + 1]

# Example usage     
s = "babad"
print(longest_palindrome(s))  # Output: "bab" or "aba"
s = "cbbd"
print(longest_palindrome(s))  # Output: "bb"

# Time Complexity: O(n^2)
# Space Complexity: O(1)