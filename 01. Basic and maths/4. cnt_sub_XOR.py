# Count Subarrays with XOR = K
# You are given:
# An array of integers
# An integer K
# 👉 You have to count how many contiguous subarrays have XOR equal to K.


# Optimal ✅: Prefix XOR + HashMap
# Idea
# If prefix_xor ^ previous_xor = K
# Then subarray XOR = K


# def count_subarrays_with_xor(arr, K):
#     count = 0
#     prefix_xor = 0
#     freq = {0: 1}  # To handle the case when prefix_xor itself is K

#     for num in arr:
#         prefix_xor ^= num
#         required_xor = prefix_xor ^ K
#         count += freq.get(required_xor, 0)
#         freq[prefix_xor] = freq.get(prefix_xor, 0) + 1

#     return count

def count_subarrays_xor_k(arr, k):
    xor_map = {}
    curr_xor = 0
    count = 0

    for num in arr:
        curr_xor ^= num
 
        if curr_xor == k:
            count += 1

        if (curr_xor ^ k) in xor_map:
            count += xor_map[curr_xor ^ k]

        xor_map[curr_xor] = xor_map.get(curr_xor, 0) + 1

    return count

print(count_subarrays_xor_k([4, 2, 2, 6, 4], 6))  # 4

# ⏱ Time: O(n)
# 📦 Space: O(n)