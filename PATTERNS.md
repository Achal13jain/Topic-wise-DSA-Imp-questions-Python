# 🧭 Pattern Cheat-Sheet

The hardest part of an interview problem is usually *recognizing which technique it wants*. This page maps the **signal** in a problem statement to the **technique** you should reach for, with an example you can open in this repo.

**How to use it:** read the signal in the left column, commit the technique to memory, then open the matching solution and study the shape of the code — not just the answer.

| When you see this signal… | Reach for | Example in this repo | Typical complexity |
| --- | --- | --- | --- |
| Sorted array, find a pair/triplet that hits a target | **Two Pointers** (converging) | Two Sum, 3Sum | `O(n)` – `O(n²)` |
| Longest/shortest contiguous window under a constraint | **Sliding Window** | Longest Substring Without Repeating | `O(n)` |
| Repeated range/subarray sum queries | **Prefix Sum** | Subarray Sum Equals K | `O(n)` |
| Need next-greater/smaller or a running min/max | **Monotonic Stack** | Next Greater Element, Largest Rectangle | `O(n)` |
| Fast lookup, dedup, or group-by-frequency | **Hash Map / Set** | Group Anagrams, Top K Frequent | `O(n)` |
| Shortest path in an unweighted grid or graph | **BFS** | Number of Islands, Rotting Oranges | `O(V+E)` |
| Explore every path / count connected components | **DFS** | Number of Islands, Clone Graph | `O(V+E)` |
| Order tasks with dependencies / detect a cycle | **Topological Sort** | Course Schedule | `O(V+E)` |
| Shortest path with weighted edges | **Dijkstra** (min-heap) | Network Delay Time | `O(E log V)` |
| Group connected items / dynamic connectivity | **Union-Find (DSU)** | Number of Provinces | `~O(n·α(n))` |
| Top K, K smallest, or a streaming median | **Heap / Priority Queue** | Kth Largest, Merge K Sorted | `O(n log k)` |
| Generate all subsets/permutations/combinations | **Backtracking** | Subsets, N-Queens | exponential |
| Search a sorted or monotonic answer space | **Binary Search** | Search Rotated Array, Book Allocation | `O(log n)` |
| Overlapping subproblems + optimal substructure | **Dynamic Programming** | Coin Change, LIS, Edit Distance | often `O(n²)` |
| A locally optimal choice yields a global optimum | **Greedy** | Merge Intervals, Job Sequencing | `O(n log n)` |
| Reverse/reorder nodes, or detect a loop | **Slow/Fast Pointers** | Reverse Linked List, Cycle Detection | `O(n)` |
| Odd-one-out, toggles, power-of-two checks | **Bit Manipulation** (XOR, masks) | XOR Properties, Power of Two | `O(1)` - `O(n)` |

---

### A 30-second decision flow

1. **Is the input sorted, or can sorting it help?** → think Two Pointers or Binary Search before anything else.
2. **Is it about a contiguous run (subarray/substring)?** → Sliding Window or Prefix Sum.
3. **Is it a grid, network, or "connected" relationship?** → it's a graph → BFS / DFS / Union-Find.
4. **Are you asked for "all the ways" to do something?** → Backtracking.
5. **Are you asked for an optimum and choices overlap?** → Dynamic Programming. If choices are independent and greedy-safe → Greedy.
6. **Do you need the K best / a running order?** → Heap.

> If two techniques fit, pick the one with the better worst-case complexity, then state the trade-off out loud in the interview — that reasoning is often what's actually being tested.
