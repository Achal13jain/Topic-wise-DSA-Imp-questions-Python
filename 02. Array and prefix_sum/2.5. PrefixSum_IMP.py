# 1. Prefix Sum Array Implementation

def prefix_sum(arr):
    """Compute the prefix sum array of the given list.

    Args:
        arr (list of int/float): The input array.

    Returns:
        list of int/float: The prefix sum array.
    """
    if not arr:
        return []

    prefix_sum_arr = [0] * len(arr)
    prefix_sum_arr[0] = arr[0]

    for i in range(1, len(arr)):
        prefix_sum_arr[i] = prefix_sum_arr[i - 1] + arr[i]

    return prefix_sum_arr

# Example usage
arr=[1, 2, 3, 4, 5]
print("Original array:", arr)
print("Prefix sum array:", prefix_sum(arr))

# Output:
# Original array: [1, 2, 3, 4, 5]   
# Prefix sum array: [1, 3, 6, 10, 15]

# Time complexity: O(n)
# Space complexity: O(n)


# 2. Subarray Sum using Prefix Sum Array

# Logic:
# arr = [2, 4, 6, 8]
# prefix = [2, 6, 12, 20]
# sum(1 to 3) = prefix[3] - prefix[0]
#             = 20 - 2
#             = 18


def subarray_sum(arr, left, right):
    """Compute the sum of the subarray from index left to right using prefix sum array.

    Args:
        arr (list of int/float): The input array.
        left (int): The starting index of the subarray (inclusive).
        right (int): The ending index of the subarray (inclusive).
    Returns:
        int/float: The sum of the subarray from left to right.
    """
    if left < 0 or right >= len(arr) or left > right:
        raise ValueError("Invalid left or right indices")

    prefix_sum_arr = prefix_sum(arr)

    if left == 0:
        return prefix_sum_arr[right]
    else:
        return prefix_sum_arr[right] - prefix_sum_arr[left - 1]
     
# Example usage
arr = [1, 2, 3, 4, 5]
left = 1
right = 3
print("Subarray sum from index", left, "to", right, ":", subarray_sum(arr, left, right))
# Output:
# Subarray sum from index 1 to 3 : 9

# Time complexity: O(n) for prefix sum array computation, O(1) for subarray sum query
# Space complexity: O(n) for prefix sum array

# 3. Total sum of all subarrays using Prefix Sum Array

# Logic:
# arr = [1, 2, 3]
# Total sum of all subarrays = 1*3 + 2*4 + 3*3 = 20
# Explanation:
# Element 1 at index 0 appears in 3 subarrays: [1], [1,2], [1,2,3]
# Element 2 at index 1 appears in 4 subarrays: [2], [1,2], [2,3], [1,2,3]
# Element 3 at index 2 appears in 3 subarrays: [3], [2,3], [1,2,3]
# Total = 1*3 + 2*4 + 3*3 = 20

def total_subarray_sum(arr):
    """Compute the total sum of all subarrays using prefix sum array.

    Args:
        arr (list of int/float): The input array.

    Returns:
        int/float: The total sum of all subarrays.
    """
    n = len(arr)
    prefix_sum_arr = prefix_sum(arr)
    total_sum = 0

    for i in range(n): # Iterate through each element in the array 
        total_sum += arr[i] * (i + 1) * (n - i) # Contribution of arr[i] to total sum of all subarrays

    return total_sum

# Example usage
arr = [1, 2, 3]
print("Total sum of all subarrays:", total_subarray_sum(arr))
# Output:
# Total sum of all subarrays: 20
# Time complexity: O(n)
# Space complexity: O(n)