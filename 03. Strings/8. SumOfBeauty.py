# The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

# For example, the beauty of "abaacc" is 3 - 1 = 2.
# Given a string s, return the sum of beauty of all of its substrings.

 

# Example 1:

# Input: s = "aabcb"
# Output: 5
# Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
# Example 2:

# Input: s = "aabcbaa"
# Output: 17

def beautySum(self, s: str) -> int:
    n = len(s)
    total = 0

    # Loop over all substrings
    for i in range(n):
        freq = {}

        for j in range(i, n):
            # Increment frequency
            freq[s[j]] = freq.get(s[j], 0) + 1

            values = freq.values()
            maxi = max(values)
            mini = min(values)

            # Add difference
            total += (maxi - mini)

    return total