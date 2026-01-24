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
    jobs.sort(reverse=True, key=lambda x: x[0])

    max_deadline = max(job[1] for job in jobs)
    slots = [-1] * (max_deadline + 1)
    total_profit = 0

    for profit, deadline in jobs:
        for d in range(deadline, 0, -1):
            if slots[d] == -1:
                slots[d] = profit
                total_profit += profit
                break

    return total_profit

# Time Complexity O(n²)
# Space Complexity O(n)