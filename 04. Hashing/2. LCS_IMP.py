# Longest Consecutive Sequence
# 🔹 Problem
# Find length of longest consecutive elements sequence
# (no need to be contiguous).

# 🔹 Idea (HashSet)
# Only start counting when number is start of sequence
# Avoid redundant work

def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Start only if num is sequence start
        if num - 1 not in num_set:
            current = num
            length = 1

            # Count consecutive numbers
            while current + 1 in num_set:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest

# Example usage:
nums = [100, 4, 200, 1, 3, 2]
result = longest_consecutive(nums)
print(result)  # Output: 4  # Explanation: The longest consecutive sequence is [1, 2, 3, 4]

# ⏱ Time: O(n)
# 📦 Space: O(n)