# Given a sorted array and a target value,
# find the index of the target. If not found, return -1.
# Binary search works because the array is sorted.

# 🔹 Idea
# Compare mid element with target
# If equal → return
# If target is smaller → search left half
# If target is larger → search right half

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1   # Search right half
        else:
            right = mid - 1  # Search left half

    return -1

# Time Complexity O(log n)
# Space Complexity O(1)