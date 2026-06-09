"""
Clone Graph (Medium)
LeetCode/Source: https://leetcode.com/problems/clone-graph/

Problem:
    Given a reference to a node in an undirected connected graph, return
    a deep copy (clone) of the graph. Each node contains a value (int)
    and a list of its neighbours.

Approach:
    DFS with a hashmap (old_node → cloned_node). When we visit a node
    for the first time we create its clone and store it. Then we
    recursively clone every neighbour and wire up the adjacency list of
    the clone.

Time:  O(V + E)  — every node and edge is visited once
Space: O(V)      — hashmap + recursion stack
"""

from __future__ import annotations
from collections import deque
from typing import Optional


class Node:
    """Graph node with a value and a list of neighbours."""

    def __init__(self, val: int = 0, neighbours: list | None = None) -> None:
        self.val = val
        self.neighbours: list[Node] = neighbours if neighbours is not None else []


def clone_graph(node: Optional[Node]) -> Optional[Node]:
    """Return a deep clone of the connected graph rooted at `node`."""
    if node is None:
        return None

    cloned: dict[Node, Node] = {}

    def dfs(n: Node) -> Node:
        if n in cloned:
            return cloned[n]
        clone = Node(n.val)
        cloned[n] = clone
        for neighbour in n.neighbours:
            clone.neighbours.append(dfs(neighbour))
        return clone

    return dfs(node)


# ---------------------------------------------------------------------------
# Helper utilities for the demo
# ---------------------------------------------------------------------------

def build_graph(adj: list[list[int]]) -> Optional[Node]:
    """Build a graph from 1-indexed adjacency list; return node 1."""
    if not adj:
        return None
    nodes = [Node(i + 1) for i in range(len(adj))]
    for i, neighbours in enumerate(adj):
        nodes[i].neighbours = [nodes[j - 1] for j in neighbours]
    return nodes[0]


def graph_to_adj(node: Optional[Node]) -> list[list[int]]:
    """Reconstruct adjacency list from a graph node (BFS, for display)."""
    if node is None:
        return []
    visited: set[int] = set()
    result: list[list[int]] = []
    queue: deque = deque([node])  # deque for O(1) popleft
    visited.add(node.val)
    while queue:
        curr = queue.popleft()
        result.append(sorted(n.val for n in curr.neighbours))
        for nb in curr.neighbours:
            if nb.val not in visited:
                visited.add(nb.val)
                queue.append(nb)
    return result


if __name__ == "__main__":
    # Graph: [[2,4],[1,3],[2,4],[1,3]]
    adj = [[2, 4], [1, 3], [2, 4], [1, 3]]
    original = build_graph(adj)
    cloned = clone_graph(original)

    print("Original adjacency list:", graph_to_adj(original))
    print("Cloned  adjacency list:", graph_to_adj(cloned))
    # Expected: [[2, 4], [1, 3], [2, 4], [1, 3]] for both

    # Verify it's a deep copy (different node objects)
    print("Same object?", original is cloned)
    # Expected: False

    # Single node, no neighbours
    solo = Node(1)
    cloned_solo = clone_graph(solo)
    print("Single node clone val:", cloned_solo.val, "| neighbours:", cloned_solo.neighbours)
    # Expected: val=1, neighbours=[]