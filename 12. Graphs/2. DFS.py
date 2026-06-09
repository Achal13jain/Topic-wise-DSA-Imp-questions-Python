"""
DFS — Depth-First Search (Medium)
LeetCode/Source: General graph traversal template

Problem:
    Given an undirected graph represented as an adjacency list and a
    starting node, visit all reachable nodes using DFS. Return the
    order in which nodes are visited.

Approach:
    Recursive DFS: call recursively on every unvisited neighbour.
    Iterative DFS: replace the call stack with an explicit stack
    (push neighbours in reverse order to match recursive order).

Time:  O(V + E)  — every vertex and edge is processed once
Space: O(V)      — visited set + recursion/explicit stack
"""

from typing import List, Dict


def dfs_recursive(
    graph: Dict[int, List[int]],
    node: int,
    visited: set,
    order: List[int],
) -> None:
    """Visit `node` and recurse on all unvisited neighbours."""
    visited.add(node)
    order.append(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs_recursive(graph, neighbour, visited, order)


def dfs(graph: Dict[int, List[int]], start: int) -> List[int]:
    """Return DFS traversal order (recursive) starting from `start`."""
    visited: set = set()
    order: List[int] = []
    dfs_recursive(graph, start, visited, order)
    return order


def dfs_iterative(graph: Dict[int, List[int]], start: int) -> List[int]:
    """Return DFS traversal order (iterative) starting from `start`."""
    visited: set = set()
    order: List[int] = []
    stack: List[int] = [start]

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        # Push in reverse so leftmost neighbour is processed first
        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append(neighbour)

    return order


if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1],
        4: [1],
        5: [2],
    }

    print("DFS (recursive) from 0:", dfs(graph, 0))
    # Expected: [0, 1, 3, 4, 2, 5]

    print("DFS (iterative) from 0:", dfs_iterative(graph, 0))
    # Expected: [0, 1, 3, 4, 2, 5]

    # Disconnected graph — DFS only visits reachable nodes
    graph2 = {0: [1], 1: [0], 2: [3], 3: [2]}
    print("DFS from 0 (disconnected):", dfs(graph2, 0))
    # Expected: [0, 1]  (nodes 2,3 are unreachable from 0)
