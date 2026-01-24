# Sieve of Eratosthenes
# 🔹 Problem Statement (What is the question?)
# You are given an integer n.
# You must find all prime numbers from 2 to n.

# ❗ Why is this a problem?

# Checking each number for primality individually takes:
# O(n√n)  ❌
# This is too slow for large n (like 10⁶ or more).

# 📌 Example
# Input:  n = 30
# Output: 2 3 5 7 11 13 17 19 23 29

# 🔹 Idea / Approach (Sieve Logic)
# Key Observations

# A prime number has no divisors other than 1 and itself.
# Every composite number has a prime factor ≤ √n.

# Core Idea

# Assume all numbers are prime
# Start marking multiples of each prime as non-prime
# Start marking from p*p because smaller multiples are already handled

# 🔹 Optimal DSA Solution (Pure Logic)
def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False

    p = 2
    while p * p <= n:
        if is_prime[p]:
            i = p * p
            while i <= n:
                is_prime[i] = False
                i += p
        p += 1

    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)

    return primes

print(sieve_of_eratosthenes(30))

# Time: O(n log log n)
# Space: O(n)