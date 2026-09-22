"""
Problem: Job Sequencing Problem
LeetCode: N/A (GeeksForGeeks Classic)

Time Complexity: O(n^2) (Can be optimized to O(n log n) with Disjoint Set)
Space Complexity: O(n)
Why optimal: Greedy choice of doing the most profitable job as late as possible ensures maximum profit.
"""

# Each job has:
# Deadline
# Profit
# You can do only one job at a time.
# Goal:
# Maximize total profit.

# 🔹 Greedy Idea
# Sort jobs by profit (descending)
# Schedule each job as late as possible before its deadline

def job_sequencing(jobs):
    # jobs = [(profit, deadline)]
    if not jobs:
        return 0
    ordered_jobs = sorted(jobs, reverse=True, key=lambda x: x[0])

    max_deadline = max(job[1] for job in ordered_jobs)
    slots = [-1] * (max_deadline + 1)
    total_profit = 0

    for profit, deadline in ordered_jobs:
        for d in range(deadline, 0, -1):
            if slots[d] == -1:
                slots[d] = profit
                total_profit += profit
                break

    return total_profit

# Time Complexity O(n²)
# Space Complexity O(n)
