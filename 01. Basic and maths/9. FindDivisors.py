"""
Problem: Find all divisors of a number

Given a positive integer ``n``, return all of its positive divisors in
ascending order.

Approach:
    Check possible factors only from 1 through sqrt(n). When ``i`` divides
    ``n``, both ``i`` and ``n // i`` are divisors. For a perfect square,
    add the square root only once.

Time Complexity: O(sqrt(n) + d log d), where d is the number of divisors
Space Complexity: O(d)
"""

from math import isqrt


def find_divisors(n: int) -> list[int]:
    """Return the positive divisors of ``n`` in ascending order."""
    if n <= 0:
        return []

    answer = []
    for divisor in range(1, isqrt(n) + 1):
        if n % divisor == 0:
            answer.append(divisor)

            paired_divisor = n // divisor
            if divisor != paired_divisor:
                answer.append(paired_divisor)

    return sorted(answer)


class Solution:
    """Online-judge-compatible solution wrapper."""

    def divisors(self, n: int) -> list[int]:
        return find_divisors(n)


if __name__ == "__main__":
    assert find_divisors(1) == [1]
    assert find_divisors(36) == [1, 2, 3, 4, 6, 9, 12, 18, 36]
    assert Solution().divisors(13) == [1, 13]
    print("All tests passed!")
