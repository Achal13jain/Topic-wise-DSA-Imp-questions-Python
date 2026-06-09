# 🧰 How to Choose a Data Structure

`PATTERNS.md` tells you *which technique* a problem wants. This page is one level lower: once you know the technique, **which container do you put the data in so the operations you need are fast?** Picking the wrong structure is what turns a clean `O(n)` idea into a `TLE`.

The whole skill comes down to three questions. Ask them in order:

1. **What operation must be fast?** (lookup? min/max? insert at ends? sorted order?)
2. **Do I need ordering?** (insertion order, sorted order, or none?)
3. **Do I need uniqueness or key→value mapping?**

Your answers point at one structure almost every time. The tables below are just that logic, pre-computed.

---

## 1. When the problem *says* this → reach for this

The fastest way to choose: match the wording of the problem to a structure.

| The problem mentions… | Reach for | Why |
| --- | --- | --- |
| "unique", "seen before", "contains duplicate" | **Set** (`set`) | O(1) membership test |
| "count", "frequency", "most common", "anagram" | **Hash map / Counter** (`Counter`) | O(1) tally per element |
| "key → value", "look up by id", "cache" | **Hash map** (`dict`) | O(1) keyed access |
| "top K", "K largest/smallest", "median of a stream" | **Heap** (`heapq`) | O(log n) to keep the best K |
| "next greater", "nearest smaller", "valid parentheses" | **Stack** | LIFO matches the access order |
| "sliding window max/min", "first negative in window" | **Monotonic Deque** (`deque`) | O(1) push/pop at both ends |
| "process in arrival order", "level by level", "BFS" | **Queue** (`deque`) | FIFO |
| "shortest path", "connected", "network", "grid" | **Graph** (adjacency list = `dict[node] → list`) | models relationships |
| "starts with", "prefix", "autocomplete", "dictionary" | **Trie** | O(L) prefix lookup |
| "merge groups", "are these connected", "count islands by union" | **Union-Find (DSU)** | near-O(1) grouping |
| "keep sorted", "floor/ceil", "kth smallest with inserts" | **Balanced BST / sorted list** (`SortedList`) | O(log n) ordered ops |
| "range sum/min with updates" | **Fenwick / Segment Tree** | O(log n) query + update |
| "LRU cache", "most-recently-used" | **Hash map + Doubly Linked List** | O(1) move-to-front |

---

## 2. When you need this *operation* fast → use this

The same idea, indexed by capability instead of wording.

| I need fast… | Best structure | Operation cost |
| --- | --- | --- |
| Lookup / insert / delete by key | Hash map (`dict`) | O(1) average |
| Membership test | Hash set (`set`) | O(1) average |
| Index access (`a[i]`) | Dynamic array (`list`) | O(1) |
| Insert / remove at **both ends** | `deque` | O(1) |
| Insert / remove at **one end** (LIFO/FIFO) | Stack / Queue | O(1) |
| Repeated **min or max** retrieval | Heap (`heapq`) | O(log n) push/pop, O(1) peek |
| Elements **always in sorted order** | Balanced BST / `SortedList` | O(log n) |
| **Prefix** matching on strings | Trie | O(L) |
| **Grouping / connectivity** queries | Union-Find | ~O(1) amortized |
| **Range** queries with updates | Segment Tree / Fenwick | O(log n) |

> Rule of thumb: if you find yourself **scanning the whole collection** (`for x in data`) inside another loop just to find one element, you almost certainly want a hash map, a heap, or a sorted structure instead.

---

## 3. The Python toolbox (what to actually `import`)

Since this repo is Python 3, here's the concrete mapping from "I want X" to the standard-library type.

| You want | Use | Note |
| --- | --- | --- |
| Hash map | `dict` | also `collections.defaultdict` for auto-default values |
| Hash set | `set` | `frozenset` if you need it hashable |
| Frequency count | `collections.Counter` | `.most_common(k)` is handy |
| Stack | `list` (`append` / `pop`) | already O(1) |
| Queue / Deque | `collections.deque` | `popleft()` is O(1) (a `list` is O(n)) |
| Min-heap | `heapq` | for a **max-heap**, push `-value` |
| Sorted container | `sortedcontainers.SortedList` | 3rd-party; or `bisect` on a list for mostly-static data |
| LRU ordering | `collections.OrderedDict` | `.move_to_end()`; or `functools.lru_cache` for memoization |
| Tuple as key | `dict[(r, c)]` | great for grids and visited-states |

---

## 4. Complexity cheat-sheet

Keep this in your head — it's what the choice ultimately rests on.

| Structure | Access | Search | Insert | Delete |
| --- | --- | --- | --- | --- |
| Array / `list` | O(1) | O(n) | O(1)* end / O(n) middle | O(n) |
| Hash map / set | — | O(1) avg | O(1) avg | O(1) avg |
| Stack / Queue (`deque`) | O(n) middle | O(n) | O(1) ends | O(1) ends |
| Heap (`heapq`) | O(1) peek | O(n) | O(log n) | O(log n) pop-min |
| Balanced BST / `SortedList` | O(log n) | O(log n) | O(log n) | O(log n) |
| Trie | — | O(L) | O(L) | O(L) |
| Union-Find | — | ~O(1) | ~O(1) | — |
| Linked List | O(n) | O(n) | O(1) at node | O(1) at node |

\* amortized

---

## 5. Composite structures (the ones that confuse people)

Some classic problems aren't *one* structure — they're two working together. These pairings come up constantly:

- **LRU Cache** = Hash map (for O(1) lookup) **+** Doubly Linked List (for O(1) reordering).
- **Median of a data stream** = a max-heap for the lower half **+** a min-heap for the upper half (the "two heaps" trick).
- **Dijkstra / weighted shortest path** = Graph (adjacency list) **+** a min-heap of `(distance, node)`.
- **Sliding-window maximum** = a **monotonic** deque that drops elements that can never be the max.
- **Counting islands / friend circles** = Grid traversal **+** Union-Find, or just BFS/DFS with a visited set.
- **Detect a cycle in a linked list** = the list **+** two pointers (slow/fast), no extra space.

---

### TL;DR decision flow

```
Need key → value lookup?           → Hash map
Just membership / uniqueness?      → Hash set
Counting things?                   → Counter
Repeated min/max or top-K?         → Heap
LIFO / FIFO / both ends?           → Stack / Queue / Deque
Must stay in sorted order?         → Balanced BST / SortedList
Prefixes / autocomplete?           → Trie
Connectivity / grouping?           → Union-Find
Relationships / paths?             → Graph
Range queries with updates?        → Segment Tree / Fenwick
```

Pair this with [`PATTERNS.md`](./PATTERNS.md): patterns tell you the *plan*, data structures tell you the *tools*.
