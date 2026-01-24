# Given arrival and departure times of trains,
# find minimum number of platforms needed so no train waits.

# 🔹 Greedy Idea
# Sort arrival and departure times separately
# If next train arrives before earlier departs → need new platform
# Otherwise → reuse platform

def min_platforms(arr, dep):
    arr.sort()
    dep.sort()

    i = 0
    j = 0
    platforms = 0
    max_platforms = 0

    while i < len(arr): # If a train arrives before or at the same time another leave
        if arr[i] <= dep[j]:# A new train came in, and no train left yet → need one more platform.
            platforms += 1
            max_platforms = max(max_platforms, platforms)
            i += 1
        else:
            platforms -= 1
            j += 1

    return max_platforms

#Example usage:
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
print(min_platforms(arr, dep))  # Output: 3

# Time complexity: O(n log n) 
# Space Complexity: O(1)