# Longest Common Subsequence
# Given two strings, find length of longest subsequence common to both.

# 🔹 DP Idea
# if s1[i] == s2[j]:
#     dp[i][j] = 1 + dp[i-1][j-1]
# else:
#     dp[i][j] = max(dp[i-1][j], dp[i][j-1])

def lcs(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

# Example usage:
text1 = "abcde"
text2 = "ace"
result = lcs(text1, text2)
print(result)  # Output: 3  # Explanation: The longest common subsequence is "ace" and its length is 3.
# Time Complexity: O(m × n) 
# Space Complexity: O(m × n)