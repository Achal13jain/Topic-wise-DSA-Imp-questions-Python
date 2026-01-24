# Given array arr and window size k,
# count distinct elements in each sliding window.

# 🔹 Idea (Sliding Window + HashMap)
# Maintain frequency map for window
# Add right element
# Remove left element

def count_distinct_in_windows(arr, k):
    if k > len(arr) or k == 0:
        return []

    freq = {}
    result = []

    # Initialize frequency map for first window
    for i in range(k):
        freq[arr[i]] = freq.get(arr[i], 0) + 1

    result.append(len(freq))

    # Slide the window
    for i in range(k, len(arr)):
        # Add new element (right end)
        freq[arr[i]] = freq.get(arr[i], 0) + 1

        # Remove old element (left end)
        left_elem = arr[i - k]
        freq[left_elem] -= 1
        if freq[left_elem] == 0:
            del freq[left_elem]

        result.append(len(freq))

    return result

# Example usage:
arr = [1, 2, 1, 3, 4, 2, 3]
k = 4
result = count_distinct_in_windows(arr, k)
print(result)  # Output: [3, 4, 3, 3]

# ⏱ Time: O(n)
# 📦 Space: O(k)