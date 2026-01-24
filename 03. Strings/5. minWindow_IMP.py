# #Find minimum window in s that contains all characters of t.

# 🔹 Idea (Sliding Window + Frequency Map)
# Expand right pointer to include all chars
# Shrink from left to minimize window

def min_window(s, t):
    if not s or not t:
        return ""

    freq = {}
    for ch in t:
        freq[ch] = freq.get(ch, 0) + 1

    left = 0
    count = len(t)
    min_len = float('inf') # Initialize to infinity
    start = 0
    
    # Expand window with right pointer
    for right in range(len(s)):
        if s[right] in freq:
            if freq[s[right]] > 0:
                count -= 1
            freq[s[right]] -= 1

        # Valid window found
        while count == 0:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                start = left

            if s[left] in freq:
                freq[s[left]] += 1
                if freq[s[left]] > 0:
                    count += 1
            left += 1

    return "" if min_len == float('inf') else s[start:start + min_len]

# Example usage
s = "ADOBECODEBANC"
t = "ABC"
print(min_window(s, t))  # Output: "BANC"
s = "a"
t = "a"
print(min_window(s, t))  # Output: "a"
s = "a"
t = "aa"
print(min_window(s, t))  # Output: ""
# Time Complexity: O(n)
# Space Complexity: O(m) where m is the size of t
