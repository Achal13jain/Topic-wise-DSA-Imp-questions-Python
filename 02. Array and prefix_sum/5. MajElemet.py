# Find the element appearing more than n/2 times.

# 🔹 Idea (Boyer-Moore Voting Algorithm)
# Cancel out different elements
# Majority always survives

def majority_element(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    return candidate
# Example usage:
nums = [3,2,3]
result = majority_element(nums)
print(result)  # Output: 3

# ⏱ Time: O(n)
# 📦 Space: O(1)