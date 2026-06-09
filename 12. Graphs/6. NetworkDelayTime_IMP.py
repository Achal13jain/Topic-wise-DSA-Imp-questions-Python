"""
Network Delay Time (Medium)
LeetCode/Source: https://leetcode.com/problems/network-delay-time/

Problem:
    There are `n` network nodes labelled 1 to n. Given a list of travel
    times `times` = [[u, v, w], ...] (directed edge u→v with weight w),
    find the minimum time for a signal sent from node `k` to reach ALL
    other nodes. Return -1 if not all nodes are reachable.

Approach:
    Single-source shortest path from k using Dijkstra's algorithm with a
    min-heap. Relax edges greedily: always process the node with the
    currently smallest known distance.

Time:  O((V + E) log V)  — each node/edge pushed to heap at most once
Space: O(V + E)           — adjacency list + dist array + heap
"""

import heapq
from typing import List
from collections import defaultdict


def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
    """Return the time for signal from k to reach all nodes, or -1."""
    graph: dict = defaultdict(list)
    for u, v, w in times:
        graph[u].append((w, v))

    dist = {i: float("inf") for i in range(1, n + 1)}
    dist[k] = 0
    min_heap = [(0, k)]  # (distance, node)

    while min_heap:
        d, node = heapq.heappop(min_heap)
        if d > dist[node]:
            continue  # stale entry
        for weight, neighbour in graph[node]:
            new_dist = d + weight
            if new_dist < dist[neighbour]:
                dist[neighbour] = new_dist
                heapq.heappush(min_heap, (new_dist, neighbour))

    max_delay = max(dist.values())
    return max_delay if max_delay != float("inf") else -1


if __name__ == "__main__":
    times1 = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    print(network_delay_time(times1, n=4, k=2))
    # Expected: 2

    times2 = [[1, 2, 1]]
    print(network_delay_time(times2, n=2, k=1))
    # Expected: 1

    times3 = [[1, 2, 1]]
    print(network_delay_time(times3, n=2, k=2))
    # Expected: -1  (node 1 not reachable from 2)
