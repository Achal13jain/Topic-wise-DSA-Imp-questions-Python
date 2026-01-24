# Count frequency of each element in an array without using collections.Counter.

# 🔹 Idea
# Use dictionary as a hashmap
# Increment count manually

def freq_count(arr):
    freq = {}
    for item in arr:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

# Example usage
arr = [1, 2, 2, 3, 1, 4, 5, 3, 2]
result = freq_count(arr)
print(result)  # Output: {1: 2, 2: 3, 3: 2, 4: 1, 5: 1}

# Time Complexity: O(n)
# Space Complexity: O(n)

# Note: This implementation assumes that the input array can contain hashable elements.

#Alternative using defaultdict from collections module
from collections import defaultdict
def freq_count_defaultdict(arr):
    freq = defaultdict(int)
    for item in arr:
        freq[item] += 1
    return dict(freq)


#alternative using .get() method of dictionary
def freq_count_get(arr):
    freq = {}
    for item in arr:
        freq[item] = freq.get(item, 0) + 1
    return freq
