"""
Number of Provinces (Medium)
LeetCode/Source: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
(equivalent to LeetCode 547 — Number of Provinces)

Problem:
    There are n cities. A 2D matrix `is_connected[i][j] = 1` means city i
    and city j are directly connected. Find the total number of provinces
    (connected components).

Approach:
    Union-Find (Disjoint Set Union). For each connected pair (i, j),
    union them. The number of distinct roots at the end equals the number
    of provinces. Uses path compression and union by rank for near-O(1)
    per operation.

Time:  O(n²)  — scan the n×n matrix; union/find is nearly O(1) amortised
Space: O(n)   — parent and rank arrays
"""

from typing import List


class UnionFind:
    """Disjoint Set Union with path compression and union by rank."""

    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.components -= 1


def find_circle_num(is_connected: List[List[int]]) -> int:
    """Return the number of connected provinces using Union-Find."""
    n = len(is_connected)
    uf = UnionFind(n)
    for i in range(n):
        for j in range(i + 1, n):
            if is_connected[i][j] == 1:
                uf.union(i, j)
    return uf.components


def find_circle_num_dfs(is_connected: List[List[int]]) -> int:
    """Return the number of provinces using DFS (alternative approach)."""
    n = len(is_connected)
    visited = [False] * n
    provinces = 0

    def dfs(city: int) -> None:
        visited[city] = True
        for neighbour in range(n):
            if is_connected[city][neighbour] == 1 and not visited[neighbour]:
                dfs(neighbour)

    for city in range(n):
        if not visited[city]:
            provinces += 1
            dfs(city)

    return provinces


if __name__ == "__main__":
    mat1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print("Provinces (UF):", find_circle_num(mat1))
    # Expected: 2

    mat2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print("Provinces (UF):", find_circle_num(mat2))
    # Expected: 3

    print("Provinces (DFS):", find_circle_num_dfs(mat1))
    # Expected: 2
