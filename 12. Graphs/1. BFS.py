"""
BFS — Breadth-First Search (Medium)
LeetCode/Source: General graph traversal template

Problem:
    Given an undirected graph represented as an adjacency list and a
    starting node, visit all reachable nodes level by level (BFS order).
    Return the order in which nodes are visited.

Approach:
    Use a queue (collections.deque). Mark nodes visited before enqueuing
    to avoid re-processing. Dequeue one node at a time, record it, then
    enqueue all unvisited neighbours.

Time:  O(V + E)  — every vertex and edge is processed once
Space: O(V)      — visited set + queue hold at most V nodes
"""

from collections import deque
from typing import List, Dict


def bfs(graph: Dict[int, List[int]], start: int) -> List[int]:
    """Return BFS traversal order starting from `start`."""
    visited: set = set()
    order: List[int] = []
    queue: deque = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return order


def bfs_shortest_path(
    graph: Dict[int, List[int]], start: int, target: int
) -> int:
    """Return the minimum number of edges from `start` to `target`, or -1."""
    if start == target:
        return 0

    visited: set = {start}
    queue: deque = deque([(start, 0)])  # (node, distance)

    while queue:
        node, dist = queue.popleft()
        for neighbour in graph[node]:
            if neighbour == target:
                return dist + 1
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, dist + 1))

    return -1  # target not reachable


if __name__ == "__main__":
    # Undirected graph as adjacency list
    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1],
        4: [1],
        5: [2],
    }

    print("BFS order from node 0:", bfs(graph, 0))
    # Expected: [0, 1, 2, 3, 4, 5]

    print("Shortest path 0 to 5:", bfs_shortest_path(graph, 0, 5))
    # Expected: 2  (0 -> 2 -> 5)

    print("Shortest path 3 to 5:", bfs_shortest_path(graph, 3, 5))
    # Expected: 4  (3 -> 1 -> 0 -> 2 -> 5)
