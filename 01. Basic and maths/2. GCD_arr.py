#GCD of an array

#Idea
# GCD is associative
# gcd(a, b, c) = gcd(gcd(a, b), c)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_array(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result = gcd(result, arr[i])
        if result == 1:
            break
    return result

print(gcd_array([24, 36, 12]))  # 12
print(gcd_array([7, 13, 29]))   # 1

#⏱ Time: O(n log max(arr))
#📦 Space: O(1)