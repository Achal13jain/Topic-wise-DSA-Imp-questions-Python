# A wizard gives you a string S. Check if it is possible to rearrange the characters of S to form a Palindrome.

def can_form_palindrome(s):
    freq = {}

    # Count frequency of each character
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    odd_count = 0

    # Count how many characters have odd frequency
    for count in freq.values():
        if count % 2 != 0:
            odd_count += 1
            if odd_count > 1:
                return False

    return True


#Optimized approach using collections.Counter
from collections import Counter
def can_form_palindrome_optimized(s):
    freq = Counter(s)
    odd_count = sum(1 for count in freq.values() if count % 2 != 0)
    return odd_count <= 1