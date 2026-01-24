# Given intervals [start, end],
# merge overlapping intervals.

# 🔹 Greedy Idea
# Sort intervals by start time
# Merge if current overlaps with previous

def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

# Time Complexity: O(n log n)
# Space Complexity: O(n)