# #Check if string is a palindrome (ignore non-alphanumeric, case insensitive).

# 🔹 Idea (Two Pointers)
# Move inward
# Compare valid characters only

def is_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        # Move left pointer to next alphanumeric
        while left < right and not s[left].isalnum():
            left += 1
        # Move right pointer to previous alphanumeric
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters (case insensitive)
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

#Example usage
print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True  
print(is_palindrome("race a car"))                             # Output: False  

# Time Complexity: O(n)
# Space Complexity: O(1)


#alternative approach: Clean the string first, then use two pointers (simpler code but uses extra space)

# def is_palindrome(s):
    
#     r=''.join([ch.lower() for ch in s if ch.isalnum()])  # Cleaned string
#     left, right = 0, len(r) - 1
#     while left < right:
#         if r[left] != r[right]:  # Compare characters from both ends
#             return False
#         left += 1
#         right -= 1
#     return True

# Example usage
# print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True  
# print(is_palindrome("race a car"))                      # Output: False  

# Time Complexity: O(n)
# Space Complexity: O(n) (increased space due to new string creation)