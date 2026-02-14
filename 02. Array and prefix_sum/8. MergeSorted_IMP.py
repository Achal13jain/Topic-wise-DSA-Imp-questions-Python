"""
Problem: Merge Sorted Array
LeetCode: https://leetcode.com/problems/merge-sorted-array/

Time Complexity: O(m + n)
Space Complexity: O(1)
Why optimal: Merges from the back to avoid shifting elements, allowing in-place modification.
"""

#Merge Sorted Array
# Idea (Two Pointers from End)
# Compare elements from the end of both arrays

def merge_sorted(nums1, m, nums2, n):
    i = m - 1  # Pointer for nums1
    j = n - 1  # Pointer for nums2
    k = m + n - 1  # Pointer for merged array

    # Merge in reverse order
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # If any elements left in nums2, add them
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
        
# Example usage:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge_sorted(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]
# ⏱ Time: O(m+n)    
# 📦 Space: O(1)