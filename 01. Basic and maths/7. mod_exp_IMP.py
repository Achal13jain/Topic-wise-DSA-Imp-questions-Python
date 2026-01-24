# Problem Statement (What is the question?)

# You are given:
# An integer a (base)
# An integer b (exponent)
# An integer m (modulus)

# You must compute:
#(a^b)mod m (that is, the remainder when a raised to the power b is divided by m).

# ❗ Why is this a problem?

# Directly computing a^b is not feasible when b is large.

# a^b grows exponentially and will:
# Cause TLE
# Cause integer overflow
# You are not allowed to use built-ins like pow(a, b, m).

# 📌 Example
# Input:  a = 2, b = 10, m = 1000
# Output: 24
# Explanation: (2^10) % 1000 = 1024 % 1000 = 24

# 🔹 Idea / Approach (Binary Exponentiation)
# Key Observations
#(a×b) % m = ((a % m)×(b % m)) % m

# Instead of computing a^b, we:
# Square a
# Reduce b by half each step
# Logic
# If b is odd → multiply result by a
# Square a
# Divide b by 2

# This reduces:
# O(b) → O(log b)

# 🔹 Optimal DSA Solution (Pure Logic)
def modular_exponentiation(a, b, m):
    result = 1
    a = a % m

    while b > 0:
        # If b is odd
        if b & 1:
            result = (result * a) % m

        # Square the base
        a = (a * a) % m

        # Divide exponent by 2
        b = b >> 1

    return result

print(modular_exponentiation(2, 10, 1000))  # 24

# ⏱ Time Complexity: O(log b)
# 📦 Space Complexity: O(1)