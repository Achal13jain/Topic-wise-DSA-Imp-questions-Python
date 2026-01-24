#check if a number is a perfect square

#Idea
# A perfect square is an integer that is the square of an integer.
#Binary search can be used to efficiently determine if a number is a perfect square.
# The algorithm works by narrowing down the possible integer values whose square could equal the given number.

def is_perfect_square(n):
    if n < 0:
        return False

    left, right = 0, n
    while left <= right:
        mid = (left + right) // 2
        sq = mid * mid

        if sq == n:
            return True
        elif sq < n:
            left = mid + 1
        else:
            right = mid - 1

    return False

print(is_perfect_square(49))  # True
print(is_perfect_square(50))  # False

#Time Complexity: O(log n)
#Space Complexity: O(1)