"""
Course Schedule (Medium)
LeetCode/Source: https://leetcode.com/problems/course-schedule/

Problem:
    There are `numCourses` courses labelled 0 to numCourses-1. Given a
    list of prerequisite pairs [a, b] (must take b before a), determine
    whether it is possible to finish all courses.

Approach:
    Model as a directed graph. The answer is "yes" if and only if the
    graph has no cycle. Use DFS with a 3-state coloring:
      0 = unvisited, 1 = in current DFS path, 2 = fully processed.
    If we reach a node that's already on the current path (state 1),
    a cycle exists.

Time:  O(V + E)  — standard DFS over courses and prerequisites
Space: O(V + E)  — adjacency list + color array + recursion stack
"""

from typing import List
from collections import defaultdict


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """Return True if all courses can be finished (no cycle exists)."""
    graph: dict = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    # 0 = unvisited | 1 = visiting (on current path) | 2 = done
    color = [0] * num_courses

    def has_cycle(node: int) -> bool:
        if color[node] == 1:
            return True   # back-edge → cycle
        if color[node] == 2:
            return False  # already fully explored, safe

        color[node] = 1
        for neighbour in graph[node]:
            if has_cycle(neighbour):
                return True
        color[node] = 2
        return False

    return not any(has_cycle(c) for c in range(num_courses) if color[c] == 0)


def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    """Return a valid course order (topological sort), or [] if impossible."""
    graph: dict = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    color = [0] * num_courses
    order: List[int] = []

    def dfs(node: int) -> bool:
        if color[node] == 1:
            return False
        if color[node] == 2:
            return True
        color[node] = 1
        for nb in graph[node]:
            if not dfs(nb):
                return False
        color[node] = 2
        order.append(node)
        return True

    for c in range(num_courses):
        if color[c] == 0 and not dfs(c):
            return []

    return order[::-1]


if __name__ == "__main__":
    print(can_finish(2, [[1, 0]]))
    # Expected: True  (take 0 then 1)

    print(can_finish(2, [[1, 0], [0, 1]]))
    # Expected: False  (0 requires 1, 1 requires 0 → cycle)

    print(find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
    # Expected: [0, 1, 2, 3] or [0, 2, 1, 3] (any valid topological order)

    print(can_finish(5, [[1, 4], [2, 4], [3, 1], [3, 2]]))
    # Expected: True
