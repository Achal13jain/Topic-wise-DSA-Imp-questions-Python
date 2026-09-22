"""
Course Schedule (Medium)
LeetCode/Source: https://leetcode.com/problems/course-schedule/

Problem:
    There are `numCourses` courses labelled 0 to numCourses-1. Given a
    list of prerequisite pairs [a, b] (must take b before a), determine
    whether it is possible to finish all courses.

Approach:
    Model prerequisites as a directed graph and use Kahn's topological
    sort. Courses with zero remaining prerequisites enter a queue. If
    every course is processed, no cycle exists.

Time:  O(V + E)  — standard DFS over courses and prerequisites
Space: O(V + E)  — adjacency list, indegrees, and queue
"""

from typing import List
from collections import defaultdict, deque


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """Return True if all courses can be finished (no cycle exists)."""
    return len(find_order(num_courses, prerequisites)) == num_courses


def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    """Return a valid course order (topological sort), or [] if impossible."""
    graph: dict = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    indegree = [0] * num_courses
    for course, _ in prerequisites:
        indegree[course] += 1

    queue = deque(course for course in range(num_courses) if indegree[course] == 0)
    order: List[int] = []

    while queue:
        course = queue.popleft()
        order.append(course)
        for next_course in graph[course]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)

    return order if len(order) == num_courses else []


if __name__ == "__main__":
    print(can_finish(2, [[1, 0]]))
    # Expected: True  (take 0 then 1)

    print(can_finish(2, [[1, 0], [0, 1]]))
    # Expected: False  (0 requires 1, 1 requires 0 → cycle)

    print(find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
    # Expected: [0, 1, 2, 3] or [0, 2, 1, 3] (any valid topological order)

    print(can_finish(5, [[1, 4], [2, 4], [3, 1], [3, 2]]))
    # Expected: True
