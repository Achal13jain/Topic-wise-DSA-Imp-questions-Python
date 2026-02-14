"""
Problem: Power of Two
LeetCode: https://leetcode.com/problems/power-of-two/

Time Complexity: O(1)
Space Complexity: O(1)
Why optimal: Uses bitwise operation (n & (n-1)) to check for single set bit in constant time.
"""

#Check if a number is a power of 2

#idea
# A number is a power of 2 if it has only one bit set in its binary representation.
# For example:
# 1 (2^0)  -> 0001
# 2 (2^1)  -> 0010
# 4 (2^2)  -> 0100
# 8 (2^3)  -> 1000
# A number n is a power of 2 if n & (n-1) == 0 and n > 0

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# def is_power_of_two(n):
#     if n <= 0:
#         return False
#     return (n & (n - 1)) == 0

# Test cases
print(is_power_of_two(1))  # True
print(is_power_of_two(2))  # True
print(is_power_of_two(3))  # False
print(is_power_of_two(4))  # True