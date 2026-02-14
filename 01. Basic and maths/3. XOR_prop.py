"""
Problem: XOR Properties and Applications
LeetCode: https://leetcode.com/problems/single-number/

Time Complexity: O(n) for finding unique element
Space Complexity: O(1)
Why optimal: Uses XOR properties (a^a=0, a^0=a) to find unique elements without extra space.
"""

# Key Properties
# A ^ A = 0
# A ^ 0 = A
# XOR is associative & commutative

# Find unique element

def find_unique(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

print(find_unique([2, 3, 2, 4, 4]))  # 3

# ⏱ Time: O(n)
# 📦 Space: O(1)

#XOR Applications

# 1. Finding Two Unique Numbers: Given an array where every element appears twice except for two elements, find those two unique numbers.
# Solution: XOR all numbers in the array to get a final XOR sum (X). This sum X is the XOR of the two unique numbers. 
# By identifying a set bit in X (which indicates where the two unique numbers have different bits),     
# you can partition the original array into two groups and XOR each group separately to isolate the two unique numbers.
# 
# 2. Finding the Missing Number: Given an array of (n-1) distinct integers in the range from 1 to (n), find the missing number.
# Solution: XOR all the numbers from 1 to (n), and then XOR all the numbers present in the input array. The result is the missing number.
# 
arr=[1,2,3,6,5,7]

def xr(arr):
    n=len(arr)
    result=0
    r2=0
    for i in range(1,n):
        result^=i
        r2^=arr[i]
    return r2^result

print(xr(arr))


# 3. Swapping Two Variables Without a Temporary Variable: A classic programming trick to swap the values of two integers a and b in-place.
# Solution:a = a ^ b;
#          b = a ^ b; // b becomes the original value of a
#          a = a ^ b; // a becomes the original value of b

# 4. Parity Check/Error Detection: Used in networking and data storage to detect accidental changes in data bits (checksums).
#   Solution: By XORing all bits together, you can determine if the number of 1s is odd or even, which helps in error detection.    
# 5. Checking Opposite Signs: Determine if two numbers have opposite signs without conditional statements by checking if (num1 ^ num2) < 0.
# 
# 6. Toggling Bits: The XOR operator can be used to flip individual bits in a number. For example, x ^ 1 flips the least significant bit of x.
#       This is useful in scenarios like bit manipulation tasks and certain algorithms.                                                                                                                                                                             
# 7. Simple Encryption: XOR is a fundamental part of many encryption algorithms, especially simple ones like the one-time pad, because the operation is reversible (A ^ B = C implies C ^ B = A).
# 
# 8. XOR Linked Lists: An advanced data structure technique that uses the XOR of adjacent node addresses to store both the "next" and "previous" pointers in a single field, saving memory space. 