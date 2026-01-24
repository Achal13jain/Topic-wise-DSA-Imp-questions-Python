# You can subtract a value X from all elements in a subarray [L, R]. 
# Find the minimum number of operations to make all elements 0 
# (assuming elements are non-increasing or simple constraints). 

def minOperationsToZero(arr):
    operations = 0
    prev = 0

    for x in arr:
        if x > prev:
            operations += x - prev
        prev = x

    return operations
print(minOperationsToZero([1, 2, 3, 2, 1]))  # Output: 3

#Time complexity: O(n)
#Space complexity: O(1)