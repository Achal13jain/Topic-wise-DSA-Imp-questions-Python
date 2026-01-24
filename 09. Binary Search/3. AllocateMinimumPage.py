# Given an array where each element represents pages in a book,
# allocate books to m students such that:
# Each student gets contiguous books
# Maximum pages allocated to any student is minimized

# 🔹 Idea (Binary Search on Answer)
# Minimum possible pages = max(book pages)
# Maximum possible pages = sum of all pages
# Binary search on this range
# Check feasibility using greedy allocation

def allocate_books(pages, students):
    if students > len(pages):
        return -1

    def can_allocate(max_pages):
        count = 1
        curr_sum = 0

        for p in pages:
            if curr_sum + p > max_pages:
                count += 1
                curr_sum = p
                if count > students:
                    return False
            else:
                curr_sum += p
        return True

    left = max(pages)
    right = sum(pages)
    answer = -1

    while left <= right:
        mid = (left + right) // 2

        if can_allocate(mid):
            answer = mid
            right = mid - 1  # Try smaller maximum
        else:
            left = mid + 1

    return answer

# Time Complexity O(n log sum)
# Space Complexity O(1)