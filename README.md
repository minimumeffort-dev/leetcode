# LeetCode

I'm working through LeetCode in Python and implementing the data structures behind the problems. I keep different versions when they help compare the approaches.

The comments explain the main ideas and why the time and space costs follow from the loops, recursion, and stored data. They distinguish expected and worst-case time and account for temporary storage and returned results.

## Problems

| File | What it does |
| --- | --- |
| [two_sum.py](two_sum.py) | Finds two numbers that add up to the target using a dictionary of values already seen. |
| [merge_strings_alternately.py](merge_strings_alternately.py) | Alternates characters from two strings, then adds the remaining tail. |
| [greatest_common_divisor_of_strings.py](greatest_common_divisor_of_strings.py) | Checks that both strings share a repeating pattern, then finds its largest possible length with GCD. |
| [kids_with_the_greatest_number_of_candies.py](kids_with_the_greatest_number_of_candies.py) | Checks which kids could reach the current maximum after receiving the extra candies. |
| [can_place_flowers.py](can_place_flowers.py) | Finds valid planting spots by checking neighboring plots and skipping ahead after a placement. |
| [reverse_vowels_of_a_string.py](reverse_vowels_of_a_string.py) | Uses two pointers to swap vowels from opposite ends of the string. |
| [hash_map_separate_chaining.py](hash_map_separate_chaining.py) | Builds a hash map with buckets of key-value pairs and separate chaining. |
| [hash_set_separate_chaining.py](hash_set_separate_chaining.py) | Builds a hash set with buckets, handling collisions by keeping keys in the same bucket. |
| [group_anagrams_sorting.py](group_anagrams_sorting.py) | Groups anagrams by sorting the letters in each word. |
| [group_anagrams_letter_counts.py](group_anagrams_letter_counts.py) | Groups lowercase English anagrams using their 26 letter counts. |
| [longest_consecutive_sequence.py](longest_consecutive_sequence.py) | Uses a set and only counts consecutive runs from their first number. |
| [merge_two_sorted_lists.py](merge_two_sorted_lists.py) | Merges two sorted linked lists by reconnecting their existing nodes. |
| [remove_duplicates_from_sorted_list.py](remove_duplicates_from_sorted_list.py) | Removes repeated values from a sorted linked list by skipping duplicate nodes. |
| [remove_linked_list_elements.py](remove_linked_list_elements.py) | Removes matching nodes, including any at the beginning of the list. |
| [reverse_linked_list.py](reverse_linked_list.py) | Reverses a linked list iteratively, with a recursive version alongside it. |
| [move_zeroes.py](move_zeroes.py) | Moves zeros to the end while keeping the other values in their original order. |
| [longest_palindromic_substring_brute_force.py](longest_palindromic_substring_brute_force.py) | Checks candidate substrings directly, skipping lengths that cannot improve the answer. |
| [longest_palindromic_substring_center_expansion.py](longest_palindromic_substring_center_expansion.py) | Expands around character and gap centers to find the longest palindrome in O(n²) time. |
| [longest_palindromic_substring_manacher.py](longest_palindromic_substring_manacher.py) | Uses Manacher's algorithm to reuse palindrome symmetry and finish in O(n) time. |
| [merge_intervals.py](merge_intervals.py) | Sorts intervals by their start, then combines overlapping ranges in one pass. |
| [meeting_rooms_ii.py](meeting_rooms_ii.py) | Sorts meetings by their start and reuses rooms with a min-heap of end times. |
| [validate_binary_search_tree.py](validate_binary_search_tree.py) | Solves [LeetCode 98](https://leetcode.com/problems/validate-binary-search-tree/) by checking each node against bounds inherited from its ancestors. [Submission](https://leetcode.com/problems/validate-binary-search-tree/submissions/2169960110/). |
| [lowest_common_ancestor.py](lowest_common_ancestor.py) | Solves [LeetCode 236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) by passing targets or their shared ancestor up the tree, assuming both targets exist. |
| [construct_binary_tree_from_preorder_and_inorder.py](construct_binary_tree_from_preorder_and_inorder.py) | Solves [LeetCode 105](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) by consuming preorder roots and splitting inorder with an index map, avoiding list copies. |
| [construct_binary_tree_from_inorder_and_postorder.py](construct_binary_tree_from_inorder_and_postorder.py) | Solves [LeetCode 106](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) by reading postorder backward and building right before left, using an inorder index map for O(n) expected time. |
| [find_if_path_exists_in_graph.py](find_if_path_exists_in_graph.py) | Solves [LeetCode 1971](https://leetcode.com/problems/find-if-path-exists-in-graph/) with BFS, using a queue and a boolean visited list to explore each vertex once. |
| [number_of_provinces.py](number_of_provinces.py) | Solves [LeetCode 547](https://leetcode.com/problems/number-of-provinces/) by starting BFS from each unvisited city and counting the connected groups in the matrix. |
| [clone_graph.py](clone_graph.py) | Solves [LeetCode 133](https://leetcode.com/problems/clone-graph/) with recursive DFS, keeping one copy per original node so cycles and shared neighbours reuse the same copies. |
| [number_of_connected_components.py](number_of_connected_components.py) | Solves [LeetCode 323](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) with union-find, using component sizes and path halving to keep searches short and counting only successful merges. |
| [number_of_islands.py](number_of_islands.py) | Solves [LeetCode 200](https://leetcode.com/problems/number-of-islands/) with BFS, counting each group of horizontally or vertically connected land cells while leaving the grid unchanged. |
| [graph_valid_tree.py](graph_valid_tree.py) | Solves [LeetCode 261](https://leetcode.com/problems/graph-valid-tree/) by checking the edge count, then using a DFS stack to detect cycles and confirm every node is connected, including long chains. |
| [pacific_atlantic_water_flow.py](pacific_atlantic_water_flow.py) | Solves [LeetCode 417](https://leetcode.com/problems/pacific-atlantic-water-flow/description/) with reverse-flow DFS stacks, moving inland to equal or higher cells and returning cells reached from both oceans. |
| [binary_tree_level_order_traversal.py](binary_tree_level_order_traversal.py) | Solves [LeetCode 102](https://leetcode.com/problems/binary-tree-level-order-traversal/) with BFS, processing one level at a time and queuing only children that exist. |
| [walls_and_gates.py](walls_and_gates.py) | Solves [LeetCode 286](https://leetcode.com/problems/walls-and-gates/) with multi-source BFS, updating rooms in place and using assigned distances to track which rooms have been visited. |
| [rotting_oranges.py](rotting_oranges.py) | Solves [LeetCode 994](https://leetcode.com/problems/rotting-oranges/) with multi-source BFS, processing one minute per queue level and returning -1 when fresh oranges remain unreachable. |
| [shortest_path_in_binary_matrix.py](shortest_path_in_binary_matrix.py) | Solves [LeetCode 1091](https://leetcode.com/problems/shortest-path-in-binary-matrix/) with BFS in eight directions, counting cells in the shortest clear path and leaving the grid unchanged. |
| [binary_tree_vertical_order_traversal.py](binary_tree_vertical_order_traversal.py) | Solves [LeetCode 314](https://leetcode.com/problems/binary-tree-vertical-order-traversal/) with BFS, grouping nodes by column while keeping top-to-bottom and left-to-right order, without sorting. |
| [sliding_window_median_sorted_list.py](sliding_window_median_sorted_list.py) | Finds [LeetCode 480](https://leetcode.com/problems/sliding-window-median/) window medians by updating one sorted list; each slide costs O(k) because elements shift. |
| [sliding_window_median_heaps.py](sliding_window_median_heaps.py) | Finds [LeetCode 480](https://leetcode.com/problems/sliding-window-median/) window medians with two heaps in O(n log(k+1)) time, using index tags and occasional cleanup to keep working storage O(k). |

## Algorithms and data structures

| File | What it does |
| --- | --- |
| [binary_search.py](binary_search.py) | Finds a value in a sorted list by repeatedly halving the search range. |
| [binary_search_recursive.py](binary_search_recursive.py) | Searches a sorted list recursively using index bounds, stopping when the range is empty. |
| [binary_search_tree.py](binary_search_tree.py) | Recursively searches a BST by choosing one child at each node, with test examples for balanced trees, chains and empty trees. |
| [bubble_sort.py](bubble_sort.py) | Swaps neighboring values until a full pass makes no changes. |
| [insertion_sort.py](insertion_sort.py) | Grows a sorted prefix by shifting larger values and inserting the next number. |
| [merge_sort.py](merge_sort.py) | Recursively sorts two halves, then merges them back into the original list. |
| [quick_sort.py](quick_sort.py) | Sorts in place with a random pivot and two-way partitioning. |
| [hash_table_double_hashing.py](hash_table_double_hashing.py) | Uses a second hash to handle collisions in a fixed-size table. |
| [max_heap.py](max_heap.py) | Implements a max heap with insertion, removal of the maximum, and sifting in both directions. |
| [build_max_heap.py](build_max_heap.py) | Builds a max heap from an existing list by sifting parents down from the bottom. |
| [doubly_linked_list.py](doubly_linked_list.py) | Implements a doubly linked list with head insertion, search, deletion, and a readable display. |
| [binary_tree_traversals.py](binary_tree_traversals.py) | Defines a binary-tree node with recursive `preorder()`, `inorder()`, and `postorder()` methods and a sideways tree display. |
| [binary_tree_sum.py](binary_tree_sum.py) | Builds a binary tree, prints it sideways, and recursively sums its values. |
| [factorial_and_fibonacci.py](factorial_and_fibonacci.py) | Practices direct recursion with factorial and Fibonacci, including zero base cases and checks for negative inputs. |
| [running_median_insertion_sort_compact.py](running_median_insertion_sort_compact.py) | Prints running medians with insertion sort and a compact median expression. |
| [running_median_insertion_sort.py](running_median_insertion_sort.py) | Prints running medians with insertion sort and explicit odd/even cases. |

## Running the examples

Use Python 3.10 or later. There are no third-party dependencies.

Files with a `__main__` block can be run directly:

```bash
python3 max_heap.py
python3 binary_tree_sum.py
python3 merge_sort.py
```

The problem solutions keep the class and method names expected by LeetCode. Linked-list solutions also include a node class so they can be used locally.

[AGENTS.md](AGENTS.md) records how solutions should be reviewed, documented, and published. [.gitignore](.gitignore) keeps local caches and environment files out of the repo.
