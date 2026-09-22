"""
Problem: LCM and GCD of two numbers
LeetCode: https://leetcode.com/problems/find-greatest-common-divisor-of-array/ (Similar Concept)

Time Complexity: O(log min(a, b))
Space Complexity: O(1)
Why optimal: Euclidean algorithm is the most efficient method for GCD.
"""

# Function to compute GCD and LCM of two numbers

#Idea (Euclid)
# gcd(a, b) = gcd(b, a % b)
# Keep reducing until b = 0

def gcd(a,b):
    while b!=0:
        a, b = b, a % b
    return abs(a)

#using recursion
# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)

def lcm(a,b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a,b)

# Example usage:
if __name__ == "__main__":
    print("GCD of 48 and 18 is:", gcd(48, 18))
    print("LCM of 48 and 18 is:", lcm(48, 18))

# ⏱ Time: O(log min(a, b))
# 📦 Space: O(1)
