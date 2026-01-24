# A peak element is one that is greater than its neighbors.
# Array may have multiple peaks — return any one.

# 🔹 Idea
# If mid < mid+1 → peak lies on right
# Else → peak lies on left
# Use binary search instead of linear scan

def find_peak(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        # If rising slope, peak on right
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left  # Index of peak

# Time Complexity O(log n)
# Space Complexity O(1)