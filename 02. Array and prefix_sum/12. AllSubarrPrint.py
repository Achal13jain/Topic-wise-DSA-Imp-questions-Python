"""
Problem: Print All Subarrays
LeetCode: N/A (Fundamental Concept)

Time Complexity: O(n^3)
Space Complexity: O(1)
Why optimal: Iterates through all possible start and end points and prints slices (printing is O(n)).
"""

# Print all subarrays of an array
def print_all_subarrays(arr):
    n = len(arr)
    for start in range(n):
        for end in range(start, n):
            # Print subarray from index start to end
            print(arr[start:end + 1])
            
# Example usage:
arr = [1, 2, 3]
print_all_subarrays(arr)
# Output:
# [1]
# [1, 2]    
# [1, 2, 3]
# [2]
# [2, 3]
# [3]

# ⏱ Time: O(n^3) (unavoidable as we are printing all subarrays)
# 📦 Space: O(1)

# Total number of non-empty subarrays of an array = n*(n+1)/2