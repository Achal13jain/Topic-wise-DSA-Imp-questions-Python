"""Regression tests for bugs found during the solution correctness audit."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path
from types import ModuleType


ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, relative_path: str) -> ModuleType:
    """Load a solution file whose path is not a valid Python import path."""
    module_path = ROOT / relative_path
    spec = importlib.util.spec_from_file_location(name, module_path)
    if spec is None or spec.loader is None:
        raise ImportError(relative_path)
    module = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(module_path.parent))
    try:
        spec.loader.exec_module(module)
    finally:
        sys.path.pop(0)
    return module


find_primes = load_module("find_primes", "01. Basic and maths/8. find_primes.py")
find_divisors = load_module("find_divisors", "01. Basic and maths/9. FindDivisors.py")
beauty_sum = load_module("beauty_sum", "03. Strings/8. SumOfBeauty.py")
largest_rectangle = load_module(
    "largest_rectangle",
    "06. Stack & Queue/3. LargRectangle_IMP.py",
)
dfs_module = load_module("dfs_module", "12. Graphs/2. DFS.py")
number_of_islands = load_module(
    "number_of_islands",
    "12. Graphs/3. NumberOfIslands.py",
)
course_schedule = load_module(
    "course_schedule",
    "12. Graphs/5. CourseSchedule.py",
)
tree_traversal = load_module("tree_traversal", "08. Trees/1. TreeTraversal.py")
tree_height = load_module("tree_height", "08. Trees/2. TreeHeight.py")
tree_diameter = load_module("tree_diameter", "08. Trees/3. DiameterTree.py")
tree_lca = load_module("tree_lca", "08. Trees/5. LCA.py")
tree_path_sum = load_module("tree_path_sum", "08. Trees/6. PathSum.py")
tree_max_path = load_module("tree_max_path", "08. Trees/7. MaxSumPath.py")
tree_subtree = load_module("tree_subtree", "08. Trees/8. SubTreeOfTree.py")
tree_codec = load_module("tree_codec", "08. Trees/9. Serialize&Deserialize.py")
tree_node = load_module("tree_node", "08. Trees/TreeNode.py")
lcm_gcd = load_module("lcm_gcd", "01. Basic and maths/1. LCM&GCD.py")
gcd_array = load_module("gcd_array", "01. Basic and maths/2. GCD_arr.py")
max_subarray = load_module(
    "max_subarray",
    "02. Array and prefix_sum/2. MaxSumSubArr_IMP.py",
)
sliding_window = load_module(
    "sliding_window",
    "05. Two pointers & Sliding window/2. MaxEleminWindow_IMP.py",
)
rotten_oranges = load_module("rotten_oranges", "06. Stack & Queue/4. RottenOranges.py")
reverse_linked_list = load_module("reverse_linked_list", "07. Linked List/1. ReverseLL.py")
aggressive_cows = load_module("aggressive_cows", "09. Binary Search/4. AgressiveCows.py")
monster_battle = load_module("monster_battle", "10. Greedy Problems/1. MonsterBattle_IMP.py")
minimum_platforms = load_module(
    "minimum_platforms",
    "10. Greedy Problems/2. MinimumPlatforms_IMP.py",
)
job_sequencing = load_module("job_sequencing", "10. Greedy Problems/3. JobSequencing.py")
merge_intervals = load_module("merge_intervals", "10. Greedy Problems/4. MergeInterval.py")
gas_station = load_module("gas_station", "10. Greedy Problems/5. GasStation.py")
fractional_knapsack = load_module(
    "fractional_knapsack",
    "10. Greedy Problems/6. FractionalKnapsack.py",
)
lis = load_module("lis", "11. Dynamic Programming/4. LIS.py")
max_product = load_module("max_product", "11. Dynamic Programming/8. MaxProdSubarr.py")
kth_largest = load_module("kth_largest", "13. Heap and Priority Queue/1. KthLargest.py")
combination_sum = load_module("combination_sum", "14. Backtracking/3. CombinationSum.py")
word_search = load_module("word_search", "14. Backtracking/5. WordSearch.py")


class BasicMathRegressionTests(unittest.TestCase):
    def test_find_divisors_handles_regular_square_and_boundary_inputs(self) -> None:
        self.assertEqual([], find_divisors.find_divisors(0))
        self.assertEqual([], find_divisors.find_divisors(-12))
        self.assertEqual([1], find_divisors.find_divisors(1))
        self.assertEqual([1, 2, 3, 4, 6, 9, 12, 18, 36], find_divisors.find_divisors(36))
        self.assertEqual([1, 13], find_divisors.Solution().divisors(13))

    def test_sieve_handles_values_below_two(self) -> None:
        self.assertEqual([], find_primes.sieve_of_eratosthenes(-1))
        self.assertEqual([], find_primes.sieve_of_eratosthenes(0))
        self.assertEqual([], find_primes.sieve_of_eratosthenes(1))

    def test_sieve_includes_prime_upper_bound(self) -> None:
        self.assertEqual([2], find_primes.sieve_of_eratosthenes(2))
        self.assertEqual([2, 3, 5, 7], find_primes.sieve_of_eratosthenes(7))

    def test_gcd_and_lcm_zero_and_negative_boundaries(self) -> None:
        self.assertEqual(0, lcm_gcd.lcm(0, 0))
        self.assertEqual(0, lcm_gcd.lcm(0, 7))
        self.assertEqual(12, lcm_gcd.lcm(-4, 6))
        self.assertEqual(6, lcm_gcd.gcd(-12, 18))
        self.assertEqual(0, gcd_array.gcd_array([]))


class StringRegressionTests(unittest.TestCase):
    def test_beauty_sum_has_a_standalone_function_api(self) -> None:
        self.assertEqual(0, beauty_sum.beauty_sum(""))
        self.assertEqual(5, beauty_sum.beauty_sum("aabcb"))
        self.assertEqual(17, beauty_sum.beauty_sum("aabcbaa"))


class StackRegressionTests(unittest.TestCase):
    def test_largest_rectangle_does_not_mutate_heights(self) -> None:
        heights = [2, 1, 5, 6, 2, 3]

        self.assertEqual(10, largest_rectangle.largest_rectangle_area(heights))
        self.assertEqual([2, 1, 5, 6, 2, 3], heights)

    def test_largest_rectangle_handles_empty_input(self) -> None:
        heights = []

        self.assertEqual(0, largest_rectangle.largest_rectangle_area(heights))
        self.assertEqual([], heights)

    def test_rotten_oranges_handles_empty_grid(self) -> None:
        self.assertEqual(0, rotten_oranges.oranges_rotting([]))
        self.assertEqual(0, rotten_oranges.oranges_rotting([[]]))


class LinkedListRegressionTests(unittest.TestCase):
    def test_both_reverse_entry_points_handle_a_long_list(self) -> None:
        size = 1_500
        head = reverse_linked_list.ListNode(0)
        node = head
        for value in range(1, size):
            node.next = reverse_linked_list.ListNode(value)
            node = node.next

        reversed_head = reverse_linked_list.reverse_list_recursive(head)
        values = []
        while reversed_head:
            values.append(reversed_head.val)
            reversed_head = reversed_head.next

        self.assertEqual(list(range(size - 1, -1, -1)), values)


class GraphRegressionTests(unittest.TestCase):
    def test_public_dfs_handles_a_deep_graph(self) -> None:
        size = 1_500
        graph = {node: [node + 1] for node in range(size - 1)}
        graph[size - 1] = []

        self.assertEqual(list(range(size)), dfs_module.dfs(graph, 0))

    def test_number_of_islands_handles_a_large_connected_island(self) -> None:
        grid = [["1"] * 1_500]

        self.assertEqual(1, number_of_islands.num_islands(grid))

    def test_course_schedule_handles_a_long_prerequisite_chain(self) -> None:
        size = 1_500
        prerequisites = [[course, course - 1] for course in range(1, size)]

        self.assertTrue(course_schedule.can_finish(size, prerequisites))
        self.assertEqual(list(range(size)), course_schedule.find_order(size, prerequisites))

    def test_course_schedule_still_rejects_a_cycle(self) -> None:
        prerequisites = [[1, 0], [2, 1], [0, 2]]

        self.assertFalse(course_schedule.can_finish(3, prerequisites))
        self.assertEqual([], course_schedule.find_order(3, prerequisites))


class TreeRegressionTests(unittest.TestCase):
    @staticmethod
    def build_right_chain(size: int):
        root = tree_node.TreeNode(0)
        nodes = [root]
        for value in range(1, size):
            nodes[-1].right = tree_node.TreeNode(value)
            nodes.append(nodes[-1].right)
        return root, nodes

    def test_tree_solutions_handle_a_deep_skewed_tree(self) -> None:
        size = 1_500
        root, nodes = self.build_right_chain(size)
        values = list(range(size))
        total = sum(values)

        self.assertEqual(values, tree_traversal.inorder(root))
        self.assertEqual(values, tree_traversal.preorder(root))
        self.assertEqual(values[::-1], tree_traversal.postorder(root))
        self.assertEqual(size, tree_height.height(root))
        self.assertEqual(size - 1, tree_diameter.diameter_of_binary_tree(root))
        self.assertIs(nodes[500], tree_lca.lowest_common_ancestor(root, nodes[500], nodes[-1]))
        self.assertTrue(tree_path_sum.has_path_sum(root, total))
        self.assertEqual([values], tree_path_sum.path_sum_ii(root, total))
        self.assertEqual(1, tree_path_sum.path_sum_iii(root, 0))
        self.assertEqual(total, tree_max_path.max_path_sum(root))
        self.assertTrue(tree_subtree.is_subtree(root, nodes[500]))

        encoded = tree_codec.serialize(root)
        self.assertEqual(encoded, tree_codec.serialize(tree_codec.deserialize(encoded)))

    def test_empty_tree_boundaries(self) -> None:
        self.assertTrue(tree_subtree.is_subtree(None, None))
        self.assertEqual(0, tree_max_path.max_path_sum(None))
        self.assertIsNone(tree_codec.deserialize(tree_codec.serialize(None)))

    def test_iterative_tree_solutions_preserve_branching_behavior(self) -> None:
        root = tree_node.TreeNode(10)
        root.left = tree_node.TreeNode(5)
        root.right = tree_node.TreeNode(-3)
        root.left.left = tree_node.TreeNode(3)
        root.left.right = tree_node.TreeNode(2)
        root.right.right = tree_node.TreeNode(11)
        root.left.left.left = tree_node.TreeNode(3)
        root.left.left.right = tree_node.TreeNode(-2)
        root.left.right.right = tree_node.TreeNode(1)

        self.assertEqual([3, 3, -2, 5, 2, 1, 10, -3, 11], tree_traversal.inorder(root))
        self.assertEqual(4, tree_height.height(root))
        self.assertEqual(5, tree_diameter.diameter_of_binary_tree(root))
        self.assertTrue(tree_path_sum.has_path_sum(root, 18))
        self.assertEqual(
            [[10, 5, 2, 1], [10, -3, 11]],
            tree_path_sum.path_sum_ii(root, 18),
        )
        self.assertEqual(3, tree_path_sum.path_sum_iii(root, 8))
        self.assertEqual(29, tree_max_path.max_path_sum(root))


class BoundaryRegressionTests(unittest.TestCase):
    def test_empty_array_boundaries(self) -> None:
        self.assertEqual(0, max_subarray.max_subarray([]))
        self.assertEqual(0, lis.length_of_LIS([]))
        self.assertEqual(0, max_product.max_product([]))
        self.assertEqual(-1, gas_station.gas_station([], []))
        self.assertEqual(0, job_sequencing.job_sequencing([]))

    def test_invalid_sliding_windows_return_no_windows(self) -> None:
        self.assertEqual([], sliding_window.sliding_window_max([1, 2], 0))
        self.assertEqual([], sliding_window.sliding_window_max([1, 2], 3))

    def test_empty_word_search_boundaries(self) -> None:
        self.assertFalse(word_search.exist([], "A"))
        self.assertTrue(word_search.exist([], ""))


class InputMutationRegressionTests(unittest.TestCase):
    def test_sorting_solutions_preserve_caller_inputs(self) -> None:
        monsters = [3, 1, 2]
        arrivals = [940, 900]
        departures = [1200, 910]
        jobs = [(20, 2), (100, 1)]
        intervals = [[2, 6], [1, 3]]
        items = [(60, 10), (100, 20)]
        stalls = [10, 1, 5]
        candidates = [7, 2, 3]
        numbers = [3, 2, 1, 5]

        originals = [
            list(monsters), list(arrivals), list(departures), list(jobs),
            [interval[:] for interval in intervals], list(items), list(stalls),
            list(candidates), list(numbers),
        ]
        monster_battle.can_defeat_all(monsters, 3)
        minimum_platforms.min_platforms(arrivals, departures)
        job_sequencing.job_sequencing(jobs)
        merge_intervals.merge_intervals(intervals)
        fractional_knapsack.fractional_knapsack(items, 15)
        aggressive_cows.aggressive_cows(stalls, 2)
        combination_sum.combination_sum(candidates, 7)
        kth_largest.find_kth_largest_sort(numbers, 2)

        self.assertEqual(
            originals,
            [monsters, arrivals, departures, jobs, intervals, items, stalls, candidates, numbers],
        )


if __name__ == "__main__":
    unittest.main()
